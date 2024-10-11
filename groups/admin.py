from django.contrib import admin
from .models import Attendance, Group, Student, Honadon, GroupView
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_last_name', 'student_name', 'stundet_group')
    ordering = ('student_last_name', 'student_name')
    search_fields = ('student_last_name', 'student_name')
    list_filter = ('stundet_group',)


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'para1', 'para2', 'para3', 'data_day', 'group_id')


class GroupViewAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_groups_list',)
    filter_horizontal = ('groups_list',)  # ManyToManyField uchun filter

    def get_groups_list(self, obj):
        return ", ".join([group.group_name for group in obj.groups_list.all()])
    get_groups_list.short_description = 'Groups'


admin.site.register(GroupView, GroupViewAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Group)
admin.site.register(Student, StudentAdmin)
admin.site.register(Honadon)
