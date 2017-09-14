from django.conf.urls import url
from .views import (upload_photo_artist, delete_photo_artist,
                    AlbumListView)


urlpatterns = [
    url(r'^upload/?$', upload_photo_artist, name='upload_photo_artist'),
    url(r'^(?P<photo_id>\d+)/delete/$', delete_photo_artist, name='delete_photo_artist'),
    url(r'^album/(?P<user_pk>\d+)/$', AlbumListView.as_view(), name='list_artist_albums')
    ]
