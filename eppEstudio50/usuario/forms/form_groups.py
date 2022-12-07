from django import forms
from django.contrib.auth.models import Group, Permission
from django.db.models import Q


class GroupForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['permissions'].queryset = Permission.objects.exclude(
            Q(content_type__model='permission') |
            Q(content_type__model='contenttype') |
            Q(content_type__model='session') |
            Q(content_type__model='rate') |
            Q(content_type__app_label='l10n_cuba') |
            Q(content_type__model='logentry', codename__in=['add_logentry', 'change_logentry', 'delete_logentry'])
        )

    class Meta:
        model = Group

        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'permissions': forms.SelectMultiple(attrs={'class': 'form-control'})
        }