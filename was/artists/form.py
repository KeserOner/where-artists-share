#-*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User


class RegisterArtistForm(forms.Form):
    email = forms.EmailField(label='Adresse mail', required=True)
    username = forms.CharField(label='Nom utilisateur', required=True)
    password = forms.CharField(label='Mot de passe', min_length=6, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirmation du mot de passe',
                                       min_length=6,
                                       required=True,
                                       widget=forms.PasswordInput)



    def clean(self):
        cleaned_data = super(RegisterArtistForm, self).clean()

        if 'password' in cleaned_data and 'password_confirm' in cleaned_data:
            if cleaned_data['password'] != cleaned_data['password_confirm']:
                msg = 'Les mots de passe sont différents'
                self.errors['password'] = self.error_class([msg])
                self.errors['password_confirm'] = self.error_class([msg])

            del cleaned_data['password']
            del cleaned_data['password_confirm']

        username = cleaned_data.get('username')
        self.validateUsername(username)

        email = cleaned_data.get('email')
        self.validateEmail(email)

        return cleaned_data

    def throwError(self, key=None, message=None):
        self.errors[key] = self.error_class[(message)]
