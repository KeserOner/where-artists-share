from django.contrib.auth.forms import forms
from django.forms.models import ModelForm

from .models import Artists, User


class UpdateArtistForm(ModelForm):

    error_messages = {
        'same_email': "Email already taken.",
        'same_username': "Username already taken."
    }

    username = forms.RegexField(
        label=("username"),
        max_length=100,
        regex=r'^[a-zA-Z0-9 _]+$',
        error_messages={
            'invalid': "This field must contain only letters or numbers."
        }
    )

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
