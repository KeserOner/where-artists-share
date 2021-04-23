import pytest

from django.contrib.auth.models import User
from rest_framework.test import APIClient

from artists.models import Artists


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def foobar():
    user = User.objects.create_user(
        'foobar',
        email='foobar@test.com'
    )
    user.set_password('testpwd123')
    user.save()

    return Artists.objects.create(
        user=user,
        artist_bio='A little story about me',
        artist_signature='FoObAr',
    )


@pytest.fixture
def auth_api_client(foobar):
    api_client = APIClient()
    api_client.force_authenticate(foobar.user)

    return api_client
