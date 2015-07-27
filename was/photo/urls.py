from django.conf.urls import url
from .views import upload_photo_artist, delete_photo_artist


urlpatterns = [
    url(r'^upload/?$', upload_photo_artist, name='upload_photo_artist'),
    url(r'^(?P<photo_id>\d+)/delete/$', delete_photo_artist, name='delete_photo_artist')
    ]
