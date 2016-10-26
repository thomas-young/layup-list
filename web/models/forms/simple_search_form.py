from django import forms

class SimpleSearchForm(forms.Form):
    q = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Try again...'}))
