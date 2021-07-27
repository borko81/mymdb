from django import forms

from .models import Movie, Comments


# Form connect to movie models
class NewMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ('publisher',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'plot': forms.Textarea(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'rating': forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
            'runtime': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'website': forms.DateInput(attrs={'class': 'form-control', 'type': 'text'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


# Не се ползва реших че с raw ще е по-добре, не съм решил още!
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('post', 'body',)

    def __init__(self, *args, **kwargs):
        super(CommentsForm, self).__init__(*args, **kwargs)
        self.fields['post'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control'}
        )
