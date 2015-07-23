from django.conf.urls import url
from .views import upload_photo_artist


urlpatterns = [
    url(r'^upload/?$', upload_photo_artist, name='upload_photo_artist'),
    ]
