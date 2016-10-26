from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from web.models import Course
from lib import constants
from lib.terms import is_valid_term
from dal import autocomplete


class SearchForm(forms.ModelForm):
    q = forms.ModelChoiceField(
        label='',
        # widget=forms.TextInput(attrs={
        # 'class': 'form-control',
        # 'placeholder': 'Course Search...'}),
        queryset=Course.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='course-autocomplete',
            attrs={'data-placeholder': 'Course Search...',
                   'class': 'form-control',
                   'name': 'q'}
        ))
    # q = forms.CharField(
    #     query='',
    #     widget=autocomplete.ModelSelect2(url='course-autocomplete'))

    class Meta:
        model = Course
        fields = ('q',)


# class SearchForm(forms.ModelForm):
#     class Meta:
#         model = Course
#         fields = ('title',)
#         widgets = {
#             'title': autocomplete.ModelSelect2(url='course-autocomplete')
#         }
