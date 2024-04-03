from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Journal, Category


class JournalAddView(LoginRequiredMixin, CreateView):
    model = Journal
    template_name = 'journal/add_journal.html'
    fields = ['journal_title', 'journal_description', 'journal_image', 'journal_contact', 'journal_category']
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.journal_author = self.request.user
        return super().form_valid(form)


class JournalListView(LoginRequiredMixin, ListView):
    model = Journal
    template_name = 'journal/list_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {'Categories': Category.objects.all(), "object_list": Journal.objects.all()}

    def get_queryset(self):
        queryset = Journal.objects.filter()
        if 'category' in self.request.GET:
            queryset = queryset.filter(journal_category=self.request.GET['category'])
        return queryset


class JournalDetailView(LoginRequiredMixin, DetailView):
    model = Journal
    template_name = 'journal/show_journal.html'


class JournalEditView(UserPassesTestMixin, UpdateView):
    model = Journal
    fields = ['journal_title', 'journal_description', 'journal_image', 'journal_contact', 'journal_category']
    template_name = 'journal/edit_journal.html'

    def get_success_url(self):
        return reverse_lazy('show_journal', kwargs={'pk': self.object.id})

    def test_func(self):
        jornal = (Journal.objects.get(pk=self.kwargs['pk']))
        return self.request.user == jornal.journal_author


class JournalDeleteView(LoginRequiredMixin, DeleteView):
    model = Journal
    template_name = 'journal/delete_journal.html'
    success_url = reverse_lazy('list_journal')