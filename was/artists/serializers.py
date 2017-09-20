from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from artists.models import Artists


class CreateArtistsSerializer(serializers.Serializer):

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
            'invalid': 'username must contain only letters, spaces,\
            underscores and dashes',
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
        style={'input_type': 'password'}
    )

    password2 = serializers.CharField(
        required=True,
        style={'input_type': 'password'}
    )

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords mismatch')

        return data

    def create(self, validated_data):

        user = User.objects.create_user(
            validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password1']
        )

        return Artists.objects.create(user=user)
