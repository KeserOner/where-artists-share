import pytest
import shutil

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from artists.models import Artists

pytestmark = pytest.mark.django_db


def test_create_artists(api_client):
    data = {
        "username": "foobar",
        "email": "user@email.com",
        "password1": "passwd",
        "password2": "passwd",
    }
    expected_data = {"username": "foobar", "email": "user@email.com"}

    assert not Artists.objects.count()
    response = api_client.post(reverse("artist_register"), data=data, format="json")

    assert response.status_code == 201
    assert response.json() == expected_data
    assert Artists.objects.count() == 1

    artist = Artists.objects.first()
    assert artist.user.username == data["username"]
    assert artist.user.email == data["email"]


def test_login(api_client, foobar):
    response = api_client.post(
        reverse("artist_login"),
        data={"username": foobar.user.username, "password": "testpwd123"},
    )

    assert response.status_code == 204

    response = api_client.post(
        reverse("artist_login"),
        data={"username": "dummy", "password": "testpwd123"},
        format="json",
    )

    assert response.status_code == 400
    error = response.json()["non_field_errors"]
    assert "no user with this email or username" in error

    response = api_client.post(
        reverse("artist_login"),
        data={"username": foobar.user.username, "password": "dummypwd"},
        format="json",
    )

    assert response.status_code == 400
    error = response.json()["non_field_errors"]
    assert "invalid password" in error


def test_get_artist_detail(api_client, foobar):
    banner = SimpleUploadedFile(
        name="banner.png",
        content=open("artists/tests/test_banner.png", "rb").read(),
        content_type="image/png",
    )
    profile_pic = SimpleUploadedFile(
        name="profile_pic.png",
        content=open("artists/tests/test_profile_picture.png", "rb").read(),
        content_type="image/png",
    )
    foobar.artist_banner = banner
    foobar.artist_image = profile_pic
    foobar.save()

    response = api_client.get(
        reverse("artist_detail", kwargs={"username": foobar.user.username})
    )

    assert response.status_code == 200

    data = response.json()
    assert data["username"] == foobar.user.username
    assert data["email"] == foobar.user.email
    assert data["artist_bio"] == foobar.artist_bio
    assert data["artist_signature"] == foobar.artist_signature
    assert foobar.artist_banner.url in data["artist_banner"]
    assert foobar.artist_image.url in data["artist_image"]

    shutil.rmtree(settings.MEDIA_ROOT)


def test_patch_artist_detail(auth_api_client, foobar):
    profile_pic = SimpleUploadedFile(
        name="profile_pic.png",
        content=open("artists/tests/test_profile_picture.png", "rb").read(),
        content_type="image/png",
    )
    assert not foobar.artist_image

    response = auth_api_client.patch(
        reverse("artist_detail", kwargs={"username": foobar.user.username}),
        data={"artist_image": profile_pic},
    )
    assert response.status_code == 200

    foobar.refresh_from_db()
    data = response.json()
    assert foobar.artist_image
    assert foobar.artist_image.url in data["artist_image"]

    shutil.rmtree(settings.MEDIA_ROOT)


def test_put_artist_detail(auth_api_client, foobar):
    response = auth_api_client.put(
        reverse("artist_detail", kwargs={"username": foobar.user.username}),
        data={"dummy": "dummy data"},
    )

    assert response.status_code == 405


def test_delete_artist_detail(auth_api_client, foobar):
    assert Artists.objects.count() == 1

    response = auth_api_client.delete(
        reverse("artist_detail", kwargs={"username": foobar.user.username})
    )

    assert response.status_code == 204
    assert Artists.objects.count() == 0
