from django.conf.urls import url

from .views import (
    PhotoView,
    CreatePhotoView,
    ListArtistPhotoView,
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
    url(
        r'^list/(?P<username>[A-Za-z _-]+)/$',
        ListArtistPhotoView.as_view(),
        name='list_photo_artist'
    ),
    url(
        r'^create-album/(?P<username>[A-Za-z _-]+)/$',
        CreateAlbumView.as_view(),
        name='create_album'
    ),
    url(r'^albums/(?P<user_pk>\d+)/$', AlbumListView.as_view(), name='list_artist_albums'),
    url(r'^album/(?P<pk>\d+)/$', AlbumView.as_view(), name='album_detail')
]
