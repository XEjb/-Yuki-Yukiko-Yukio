from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Yukiko
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_title(self):
        title = self.clean_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title
