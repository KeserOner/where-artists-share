#-*- coding: utf-8 -*-

from was.api import Validator
from django.contrib.auth.models import User

class CheckUserValid(Validator):
    """
    Validates username field
    """

    def validateUsername(self, value):
        msg = None
        if value:
            if value.strip() == '':
                msg = 'Le nom d\'utilisateur ne peut pas être vide.'
            elif value != value.strip():
                msg = 'Le nom d\'utilisateur ne peut pas commencer ou finir par un espace'
            elif User.objects.filter(username=value).count() > 0:
                msg = 'Ce nom est déjà utilisé'
            if msg is not None:
                self.throwError('username', msg)
        return value

    def validateEmail(self, value):
        msg = None
        if value:
            if User.objects.filter(email=value).count() > 0:
                msg = 'Cet email est déjà utilisé'
            if msg is not None:
                self.throwError('email', msg)

        return value

