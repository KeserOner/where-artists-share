#-*- coding: utf-8 -*-

from django.contrib.auth.forms import UserCreationForm
from .models import Artists, User

class CreateArtistForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super(CreateArtistForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            artist = Artists(user=user)
            artist.save()
        return user



