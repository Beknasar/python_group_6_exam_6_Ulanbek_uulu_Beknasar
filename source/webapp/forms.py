from django import forms
from .models import STATUS_CHOICES

# default_status = STATUS_CHOICES[0][0]
class SearchForm(forms.Form):
    author = forms.CharField(max_length=100, required=True, label='Имя автора записи')

    def __str__(self):
        return f'{self.name}'

class GuestForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Имя автора записи')
    email = forms.EmailField(required=True, label='Почта')
    text = forms.CharField(max_length=2000, required=True, label='Текст записи', widget=forms.Textarea)
    # status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Статус',
    #                            initial=default_status)

    def __str__(self):
        return f'{self.name} - {self.email}'