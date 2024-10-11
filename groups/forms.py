from django import forms

from groups.models import GroupView


class GroupViewForm(forms.ModelForm):
    class Meta:
        model = GroupView
        fields = ['user', 'groups_list']