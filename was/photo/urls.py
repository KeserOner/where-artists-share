from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import (upload_photo_artist, delete_photo_artist,
                    AlbumListView, CreateAlbumView)


urlpatterns = [
    url(r'^upload/?$', upload_photo_artist, name='upload_photo_artist'),
    url(r'^(?P<photo_id>\d+)/delete/$', delete_photo_artist, name='delete_photo_artist'),
    url(r'^album/(?P<user_pk>\d+)/$', AlbumListView.as_view(), name='list_artist_albums'),
    url(r'^create-album/$', login_required(CreateAlbumView.as_view()), name='create_album')
]
