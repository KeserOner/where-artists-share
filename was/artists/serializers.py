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

        return super().validate(data)

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password1'])
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
                raise serializers.ValidationError(
                    'no user with this email or username')

        auth_user = authenticate(username=user.username,
                                 password=data.get('password'))

        if not auth_user:
            raise serializers.ValidationError('invalid password')

        self._user = auth_user
        return data

    def get_user(self):
        return self._user


class ArtistSerializer(serializers.ModelSerializer):

    username = serializers.RegexField(
        r'^[A-Za-z0-9 _-]+$',
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
        },
        source='user.username'
    )

    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='This username is already used'
            )
        ],
        source='user.email'
    )

    artists_followed = serializers.SlugRelatedField(
        many=True,
        slug_field='id',
        queryset=Artists.objects.filter(user__is_active=True)
    )

    class Meta:
        model = Artists
        fields = (
            'username', 'artist_image', 'artist_banner',
            'artist_bio', 'artist_signature', 'email',
            'artists_followed', 'id'
        )
        read_only_fields = ('id',)

    def update(self, instance, validated_data):
        artists_followed_ids = validated_data.pop('artists_followed', '')
        artists_followed_qs = Artists.objects.filter(
            id__in=artists_followed_ids
        )
        instance = super(ArtistSerializer, self).update(instance,
                                                        validated_data)
        if artists_followed_qs:
            artists_followed = instance.artists_followed.all()
            for artist in artists_followed_qs:
                if artist in artists_followed:
                    instance.artists_followed.remove(artist)
                else:
                    instance.artists_followed.add(artist)

            instance.save()

        return instance


class ArtistListSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username')

    class Meta:
        model = Artists
        fields = ('id', 'username', 'artist_image')
