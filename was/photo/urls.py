from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import (
    PhotoView,
    CreatePhotoView,
    delete_photo_artist,
    AlbumListView,
    CreateAlbumView,
    AlbumView
)


urlpatterns = [
    url(r'^(?P<pk>\d+)/?$', PhotoView.as_view(), name='get_photo'),
    url(
        r'^upload/(?P<username>[A-Za-z _-]+)/$',
        CreatePhotoView.as_view(),
        name='upload_photo_artist'
    ),
    url(r'^(?P<photo_id>\d+)/delete/$', delete_photo_artist, name='delete_photo_artist'),
    url(r'^albums/(?P<user_pk>\d+)/$', AlbumListView.as_view(), name='list_artist_albums'),
    url(r'^create-album/$', login_required(CreateAlbumView.as_view()), name='create_album'),
    url(r'^album/(?P<pk>\d+)/$', AlbumView.as_view(), name='album_detail')
]
