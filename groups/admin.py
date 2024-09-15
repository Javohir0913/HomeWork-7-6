from django.contrib import admin
from .models import Attendance, Group, Student
# Register your models here.

admin.site.register(Attendance)
admin.site.register(Group)
admin.site.register(Student)