from django.contrib import admin
from .models import Attendance, Group, Student, Honadon
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_last_name', 'student_name', 'stundet_group')
    ordering = ('student_last_name', 'student_name')


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'para1', 'para2', 'para3', 'data_day', 'group_id')


admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Group)
admin.site.register(Student, StudentAdmin)
admin.site.register(Honadon)
