from django import forms
from .models import Movie


class NewMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'plot': forms.Textarea(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'rating': forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
            'runtime': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'website': forms.DateInput(attrs={'class': 'form-control', 'type': 'text'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
