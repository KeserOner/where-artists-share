# -*- coding: utf-8 -*-

from django.contrib.auth.forms import UserCreationForm, forms
from django.forms.models import ModelForm
from .models import Artists, User


class CreateArtistForm(UserCreationForm):
    error_messages = {
        'same_email': "Email already taken.",
        'password_mismatch': "Passwords mismatch.",
        'required_email': "Email is required"
    }

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(
                self.error_messages['same_email'],
                code='same_email',
            )

        if not email:
            raise forms.ValidationError(
                self.error_messages['required_email'],
                code='required_email',
            )

        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(CreateArtistForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            artist = Artists(user=user)
            artist.save()
        return user


class UpdateArtistForm(ModelForm):
    error_messages = {
        'same_email': "Email already taken.",
        'same_username': "Username already taken."
    }
    username = forms.RegexField(label=("username"), max_length=100,
                                regex=r'^[a-zA-Z0-9 _]+$',
                                error_message=("This field must contain only letters or numbers."))
    email = forms.EmailField()

    class Meta:
        model = Artists
        exclude = ['user']

    def check_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(
                self.error_messages['same_email'],
                code='same_email'
            )
        return email

    def check_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).count() > 0:
            raise forms.ValidationError(
                self.error_messages['same_username'],
                code='same_username'
            )
        return username

    def save(self):
        artist = super(UpdateArtistForm, self).save(commit=False)
        user = User.objects.get(username=artist.user.username)
        if artist.user.username != self.cleaned_data.get('username'):
            user.username = self.check_username()
        if artist.user.email != self.cleaned_data.get('email'):
            user.email = self.check_email()
        user.save()
        artist.save()
        return artist
