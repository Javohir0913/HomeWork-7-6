from django.contrib.auth import get_user_model
from django.db import models
from datetime import date

# Create your models here.
class Group(models.Model):
    group_name = models.CharField(max_length=50)
    group_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name

    class Meta:
        db_table = 'groups'
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_last_name = models.CharField(max_length=50)
    student_father_name = models.CharField(max_length=50)
    stundet_group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name

    class Meta:
        db_table = 'student'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    para1 = models.CharField(max_length=50)
    para2 = models.CharField(max_length=50)
    para3 = models.CharField(max_length=50)
    data_day = models.DateField(default=date.today)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.para1} {self.para2} {self.para3}"

    class Meta:
        db_table = 'attendance'
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'
        unique_together = (('student', 'data_day'),)
