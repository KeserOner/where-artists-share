import os

import pytest
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

pytestmark = pytest.mark.django_db


def test_image_delete_from_folder(foobar):
    banner = SimpleUploadedFile(
        name="banner.png",
        content=open("artists/tests/test_banner.png", "rb").read(),
        content_type="image/png",
    )

    assert not os.path.exists(f"{settings.MEDIA_ROOT}/artist_banner/banner.png")
    foobar.artist_banner = banner
    foobar.save()

    assert os.path.exists(f"{settings.MEDIA_ROOT}/artist_banner/banner.png")
    foobar.delete()

    assert not os.path.exists(f"{settings.MEDIA_ROOT}/artist_banner/banner.png")
