from django.urls import path

from .views import JournalAddView, JournalListView, JournalDetailView, JournalEditView, JournalDeleteView

urlpatterns = [
    path('add/', JournalAddView.as_view(), name='add_journal'),
    path('list/', JournalListView.as_view(), name='list_journal'),
    path('detail/<int:pk>/', JournalDetailView.as_view(), name='show_journal'),
    path('edit/<int:pk>/', JournalEditView.as_view(), name='edit_journal'),
    path('delete/<int:pk>/', JournalDeleteView.as_view(), name='delete_journal'),

]