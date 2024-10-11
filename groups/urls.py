from django.urls import path

from .views import GroupList, GroupAttendanceView, export_attendance_to_excel, upload_students, HonadonCreateView, \
    PDFDownloadView, PDFList, GroupViewCreate, GroupViewUpdate, GroupViewList

urlpatterns = [
    path('', GroupList.as_view(), name='group_list'),
    path('groups/<int:pk>/', GroupAttendanceView.as_view(), name='group_attendance'),
    path('Excel/<int:pk>/', export_attendance_to_excel, name='export_attendance_to_excel'),
    path('upload-students/', upload_students, name='upload_students'),
    path('honadon/create/', HonadonCreateView.as_view(), name='honadon-create'),
    path('honadon/download/<int:pk>/', PDFDownloadView.as_view(), name='honadon-download'),
    path('honadonlar/', PDFList.as_view(), name='honadon-list'),
    path('groupview/create/', GroupViewCreate.as_view(), name='groupview_create'),
    path('groupview/update/<int:pk>/', GroupViewUpdate.as_view(), name='groupview_update'),
    path('groupview/list/', GroupViewList.as_view(), name='groupview_list'),
]