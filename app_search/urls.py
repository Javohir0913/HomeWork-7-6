from django.urls import path

from .views import JournalSearchView

urlpatterns = [
    path('journal/', JournalSearchView.as_view(), name='search_journal')
]