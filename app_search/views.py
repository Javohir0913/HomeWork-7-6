from django.shortcuts import render
from django.views.generic import ListView

from app_journal.models import Journal


# Create your views here.
class JournalSearchView(ListView):
    model = Journal
    template_name = 'search/journal_search.html'

    def get_queryset(self):
        return (Journal.objects.filter(journal_title__icontains=self.request.GET['keyword']) |
                Journal.objects.filter(journal_description__icontains=self.request.GET['keyword']) |
                Journal.objects.filter(journal_contact__icontains=self.request.GET['keyword']))

