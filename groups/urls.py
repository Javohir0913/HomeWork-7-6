from django.urls import path

from .views import GroupList, GroupAttendanceView

urlpatterns = [
    path('', GroupList.as_view(), name='group_list'),
    path('groups/<int:pk>/', GroupAttendanceView.as_view(), name='group_attendance'),
]