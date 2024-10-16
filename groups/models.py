from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


# Create your models here.
class Group(models.Model):
    group_name = models.CharField(max_length=50)

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
    data_day = models.DateTimeField(default=timezone.now)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.para1} {self.para2} {self.para3}"

    class Meta:
        db_table = 'attendance'
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'
        unique_together = (('student', 'data_day'),)


class Honadon(models.Model):
    image_1 = models.ImageField(upload_to='honadon/%Y/%m/%d')
    student_name = models.CharField(max_length=255)
    image_2 = models.ImageField(upload_to='honadon/%Y/%m/%d')
    dicription = models.TextField()

    def __str__(self):
        return self.student_name

    class Meta:
        db_table = 'honadon'
        verbose_name = 'Honadon'
        verbose_name_plural = 'Honadons'


class GroupView(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    groups_list = models.ManyToManyField(Group)

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = 'groupview'
        verbose_name = 'Group View'
        verbose_name_plural = 'Group Views'
        unique_together = ('user',)
