from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Student, Attendance, Group


# Create your views here.
class GroupList(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'group/my_group.html'

    def get_queryset(self):
        # Faqat foydalanuvchi tomonidan yaratilgan guruhlarni filtrlang
        groups_data_my = Group.objects.filter(group_author=self.request.user.id)
        return groups_data_my


class GroupAttendanceView(LoginRequiredMixin, View):
    template_name = 'group/my_group_detail.html'

    def get(self, request, *args, **kwargs):
        group_id = kwargs.get('pk')
        group = Group.objects.get(id=group_id)
        students = Student.objects.filter(stundet_group=group_id)
        context = {
            'students': students,
            'group': group  # Group ob'ektini shablonga yuboryapmiz
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        group_id = kwargs.get('pk')
        group = Group.objects.get(id=group_id)
        students = Student.objects.filter(stundet_group=group_id)

        # Form ma'lumotlarini bu yerda qayta ishlash
        for student in students:
            para1 = request.POST.get(f'para1_{student.id}', False)
            para2 = request.POST.get(f'para2_{student.id}', False)
            para3 = request.POST.get(f'para3_{student.id}', False)

            # Checkbox holatiga qarab ma'lumotlarni saqlash yoki boshqa amallarni bajarish
            Attendance.objects.create(student=Student.objects.get(id=student.id), para1=para1,
                                      para2=para2, para3=para3, group_id=group)
        # Form ma'lumotlarini qayta ishlagandan keyin sahifani qayta yuklash yoki boshqa sahifaga o'tish
        return redirect('group_list')  # To'g'ri URL manzilini qo'yishingiz kerak