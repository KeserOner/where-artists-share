import pytest

from django.contrib.auth.models import User

from artists import serializers
from artists.models import Artists

pytestmark = pytest.mark.django_db


def test_artist_signup_serializer_ok():
    data = {
        'username': 'jin',
        'email': 'jin@kazama.com',
        'password1': 'pwd123',
        'password2': 'pwd123'
    }
    serializer = serializers.SignupArtistSerializer(data=data)
    assert not Artists.objects.count()
    assert serializer.is_valid()
    assert serializer.validated_data == data

    serializer.save()
    assert Artists.objects.count() == 1
    assert Artists.objects.filter(user__username=data['username'])


def test_artist_signup_serializer_ko(foobar):
    data = {
        'username': 'vegeta',
        'email': 'vegeta@sayajin.com',
        'password1': 'pwd123',
        'password2': 'pwd345'
    }

    serializer = serializers.SignupArtistSerializer(data=data)

    assert not serializer.is_valid()
    assert 'Passwords mismatch' in str(
        serializer.errors['non_field_errors'][0])

    data['email'] = 'foobar@test.com'
    data['password2'] = 'pwd123'
    serializer = serializers.SignupArtistSerializer(data=data)
    assert not serializer.is_valid()
    assert 'This email address is already used' in str(
        serializer.errors['email'][0]
    )

    data['username'] = 'veget@'
    data['email'] = 'vegeta@sayajin.com'
    serializer = serializers.SignupArtistSerializer(data=data)

    assert not serializer.is_valid()
    assert 'username must contain only letters' in str(
        serializer.errors['username'][0]
    )

    data['username'] = 'foobar'
    serializer = serializers.SignupArtistSerializer(data=data)
    assert not serializer.is_valid()
    assert 'This username is already used' in str(
        serializer.errors['username'][0]
    )

    data['username'] = 'yo'
    serializer = serializers.SignupArtistSerializer(data=data)
    assert not serializer.is_valid()
    assert '3 character long' in str(serializer.errors['username'][0])


def test_artist_signin_serializer_ok(foobar):
    data = {
        'username': 'foobar',
        'password': 'testpwd123'
    }
    serializer = serializers.SigninArtistSerializer(data=data)

    assert serializer.is_valid()
    assert serializer._user

    data['username'] = 'foobar@test.com'
    serializer = serializers.SigninArtistSerializer(data=data)

    assert serializer.is_valid()
    assert serializer._user


def test_artist_signin_serializer_ko(foobar):
    data = {
        'username': 'keser',
        'password': 'wrongpwd123'
    }
    serializer = serializers.SigninArtistSerializer(data=data)

    assert not serializer.is_valid()
    assert 'no user with this email or username' in str(
        serializer.errors['non_field_errors'][0]
    )

    data['username'] = 'foobar'
    serializer = serializers.SigninArtistSerializer(data=data)

    assert not serializer.is_valid()
    assert 'invalid password' in str(
        serializer.errors['non_field_errors'][0]
    )


def test_artist_model_serializer(foobar):
    expected_data = {
        'username': foobar.user.username,
        'artist_image': None,
        'artist_banner': None,
        'artist_bio': foobar.artist_bio,
        'artist_signature': foobar.artist_signature,
        'email': foobar.user.email,
        'artists_followed': [],
        'id': foobar.id
    }
    data = expected_data.copy()
    data['username'] = 'test'
    data['email'] = 'dummy@test.com'
    assert serializers.ArtistSerializer(data=data).is_valid()

    serializer = serializers.ArtistSerializer(instance=foobar)

    assert serializer.data == expected_data


def test_artist_model_serializer_update(foobar):
    user = User.objects.create(
        username='dummy',
        email='dummy@test.com'
    )
    user.set_password('testpwd345')
    user.save()
    artist = Artists.objects.create(user=user)

    assert not foobar.artists_followed.count()
    data = {
        'username': foobar.user.username,
        'artist_image': None,
        'artist_banner': None,
        'artist_bio': foobar.artist_bio,
        'artist_signature': foobar.artist_signature,
        'email': foobar.user.email,
        'artists_followed': [artist.id],
        'id': foobar.id
    }

    serializer = serializers.ArtistSerializer()
    validated_data = serializer.validate(attrs=data)
    serializer.update(instance=foobar, validated_data=validated_data)

    assert foobar.artists_followed.count() == 1
    assert artist in foobar.artists_followed.all()

    # if we do the same update, it should now remove the artist from the
    # foobar's followed artists
    # update poped artists_followed from validated_data though
    validated_data['artists_followed'] = [artist.id]
    serializer.update(instance=foobar, validated_data=validated_data)

    assert not foobar.artists_followed.count()


def test_artist_model_serializer_list(foobar):
    expected_data = {
        'id': foobar.id,
        'username': foobar.user.username,
        'artist_image': None
    }

    serializer = serializers.ArtistListSerializer(instance=foobar)

    assert serializer.data == expected_data
