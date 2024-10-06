from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
import pandas as pd
from django.http import HttpResponse
from datetime import timedelta
from django.utils import timezone
import pytz


from .models import Student, Attendance, Group


# Create your views here.
class GroupList(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'group/my_group.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            groups = Group.objects.all()
        else:
            groups = Group.objects.filter(group_author=self.request.user.id)

        # Create a dictionary to store student counts
        all_info = []
        for group in groups:
            all_info.append({'group': group, 'count_people': Student.objects.filter(stundet_group=group).count()})
        context['all_info'] = all_info
        return context


class GroupAttendanceView(LoginRequiredMixin, View):
    template_name = 'group/my_group_detail.html'

    def get(self, request, *args, **kwargs):
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timedelta(days=1)
        group_id = kwargs.get('pk')
        group = Group.objects.get(id=group_id)
        students = Student.objects.filter(stundet_group=group_id)
        zxc = Attendance.objects.filter(data_day__range=(today_start, today_end), group_id=group).first()
        if zxc is None:
            context = {
                'students': students,
                'group': group,  # Group ob'ektini shablonga yuboryapmiz
                'para1': 'True',
                'para2': 'False',
                'para3': 'False'
            }
        elif len(zxc.para2) == 0:
            context = {
                'students': students,
                'group': group,  # Group ob'ektini shablonga yuboryapmiz
                'para1': 'False',
                'para2': 'True',
                'para3': 'False'
            }
        elif len(zxc.para3) == 0:
            context = {
                'students': students,
                'group': group,  # Group ob'ektini shablonga yuboryapmiz
                'para1': 'False',
                'para2': 'False',
                'para3': 'True'
            }
        else:
            context = {
                'students': students,
                'group': group,  # Group ob'ektini shablonga yuboryapmiz
                'para1': 'False',
                'para2': 'False',
                'para3': 'False'
            }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timedelta(days=1)
        group_id = kwargs.get('pk')
        group = Group.objects.get(id=group_id)
        students = Student.objects.filter(stundet_group=group_id)

        # Form ma'lumotlarini bu yerda qayta ishlash
        for student in students:
            para1 = request.POST.get(f'para1_{student.id}')
            para2 = request.POST.get(f'para2_{student.id}')
            para3 = request.POST.get(f'para3_{student.id}')
            # Eski ma'lumotlarni olish (agar mavjud bo'lsa)
            attendance, created = Attendance.objects.get_or_create(
                student=student, group_id=group, data_day__range=(today_start, today_end),
            )
            # Eski qiymatlarni saqlab, faqat kelgan yangilarini yangilash
            if para1:
                attendance.para1 = para1
            if para2:
                attendance.para2 = para2
            if para3:
                attendance.para3 = para3

            # O'zgarishlarni saqlash
            attendance.save()

        # Form ma'lumotlarini qayta ishlagandan keyin sahifani qayta yuklash yoki boshqa sahifaga o'tish
        return redirect('group_list')  # To'g'ri URL manzilini qo'yishingiz kerak


def export_attendance_to_excel(request, pk):
    # Bugungi kunning boshlanish va tugash vaqtini olish
    today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = today_start + timedelta(days=1)

    # Bugungi sanaga mos ma'lumotlarni olish
    queryset = Attendance.objects.filter(data_day__range=(today_start, today_end), group_id=pk)

    # Mahalliy vaqt zonasini olish
    local_tz = pytz.timezone('Asia/Tashkent')

    # Ma'lumotlarni olish va ism-familiyani birlashtirish
    data = list(
        queryset.values('student__student_name', 'student__student_last_name', 'para1', 'para2', 'para3', 'data_day',
                        'group_id__group_name'))

    # Ism va familiyani birlashtirib yangi ro'yxat yaratish
    for item in data:
        # UTC vaqtni mahalliy vaqtga o'zgartirish
        utc_time = item['data_day'].replace(tzinfo=pytz.utc)
        local_time = utc_time.astimezone(local_tz)
        item['data_day'] = local_time.strftime('%Y-%m-%d %H:%M:%S')  # Vaqt formatlash

        item['full_name'] = item['student__student_last_name'] + ' ' + item['student__student_name']
        del item['student__student_name']
        del item['student__student_last_name']

    if not data:
        messages.warning(request, "Bugungi sana uchun bu guruhda qatnash ma'lumotlari topilmadi.")
        return redirect('group_list')  # Foydalanuvchini kerakli sahifaga yo'naltirish

    # Pandas DataFrame yaratish
    df = pd.DataFrame(data)

    # Ustunlarni tartibga solish (agar kerak bo'lsa)
    df = df[['full_name', 'para1', 'para2', 'para3', 'data_day', 'group_id__group_name']]

    # Excel fayl yaratish
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{Group.objects.get(id=pk)} {today_start.date()}.xlsx"'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Attendance')

    return response


def load_students_from_excel(file_path):
    # Excel faylini o'qish (ustunlarsiz, ya'ni header=None)
    df = pd.read_excel(file_path, header=None)
    # Har bir qatorni ma'lumotlar bazasiga saqlash
    for index, row in df.iterrows():
        # Guruhni topish yoki yaratish (D ustun - 3-indeks)
        group, created = Group.objects.get_or_create(group_name=row[3])
        print(group)
        # Talabani yaratish yoki saqlash (A, B, C ustunlar - 0, 1, 2 indekslar)
        student, created = Student.objects.get_or_create(
            student_last_name=row[0],  # A ustun - Familiya
            student_name=row[1],       # B ustun - Ism
            student_father_name=row[2],# C ustun - Otasining ismi
            stundet_group=group
        )

        print(f"Yaratildi: {student}")

    return HttpResponse("Ma'lumotlar yuklandi!")


def upload_students(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']

        # Faylni vaqtinchalik saqlash va load_students_from_excel funksiyasiga uzatish
        load_students_from_excel(excel_file)

        return HttpResponse("Ma'lumotlar bazaga yuklandi!")
    return render(request, 'upload.html')
