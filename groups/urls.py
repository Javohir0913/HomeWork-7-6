from django.urls import path

from .views import GroupList, GroupAttendanceView, export_attendance_to_excel, upload_students

urlpatterns = [
    path('', GroupList.as_view(), name='group_list'),
    path('groups/<int:pk>/', GroupAttendanceView.as_view(), name='group_attendance'),
    path('Excel/<int:pk>/', export_attendance_to_excel, name='export_attendance_to_excel'),
    path('upload-students/', upload_students, name='upload_students'),
]