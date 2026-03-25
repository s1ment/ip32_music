from django import forms
from .models import Genres

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genres
        fields = '__all__'
        labels = {
            'name_ru': 'Название на русском',
            'name_en': 'Название на английском',
            'description': 'Описание',
        }