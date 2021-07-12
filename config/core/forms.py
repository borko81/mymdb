from django import forms
from django.contrib.auth.models import User

from .models import Movie, Profile, Comments


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


# Login form
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# Register form


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password do not much')
        return cd['password']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs.update(
            {'class': 'form-control'})


# Не се ползва реших че с raw ще е по-добре.
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('post', 'body')

    def __init__(self, *args, **kwargs):
        super(CommentsForm, self).__init__(*args, **kwargs)
        self.fields['post'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control'}
        )
