#-*- coding: utf-8 -*-

from django.contrib.auth.forms import UserCreationForm, forms
from django.forms.models import ModelForm
from .models import Artists, User

class CreateArtistForm(UserCreationForm):
    error_messages = {
        'same_email': "L'email est déjà utilisé.",
    }

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(
                self.error_messages['same_email'],
                code = 'same_email',
            )
        return email

    def save(self, commit=True):
        user = super(CreateArtistForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            artist = Artists(user=user)
            artist.save()
        return user


class UpdateArtistForm(ModelForm):
    class Meta:
        model = Artists
        fields = '__all__'