from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from artists.models import Artists


class SignupArtistSerializer(serializers.Serializer):

    username = serializers.RegexField(
        r'^[a-zA-Z0-9_ -]+$',
        required=True,
        min_length=3,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='This username is already used'
            )
        ],
        error_messages={
            'invalid': 'username must contain only letters, \
                        spaces, underscores and dashes',
            'min_length': 'username must be at least 3 character long'
        }
    )

    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='This email address is already used'
            )
        ]
    )

    password1 = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    password2 = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords mismatch')

        return data

    def create(self, validated_data):

        password = validated_data['password1']
        username = validated_data['username']
        user = User.objects.create_user(
            username,
            email=validated_data['email'],
        )

        user.set_password(password)
        user.is_active = True
        user.save()

        Artists.objects.create(user=user)

        return user


class SigninArtistSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)

    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    def __init__(self, *args, **kwargs):
        self._user = None
        super().__init__(*args, **kwargs)

    def validate(self, data):
        username = data.get('username')

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            try:
                user = User.objects.get(email=username)
            except ObjectDoesNotExist:
                raise serializers.ValidationError('no user with this email \
                                                  or username')
        auth_user = authenticate(username=user.username,
                                 password=data.get('password'))

        if not auth_user:
            raise serializers.ValidationError('invalid password')

        self._user = auth_user
        return data

    def get_user(self):
        return self._user
