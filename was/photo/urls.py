from django.urls import path

from . import views


urlpatterns = [
    path('<int:pk>/', views.PhotoView.as_view(), name='get_photo'),
    path(
        'upload/<slug:username>/',
        views.CreatePhotoView.as_view(),
        name='upload_photo_artist'
    ),
    path(
        'list/<slug:username>/',
        views.ListArtistPhotoView.as_view(),
        name='list_photo_artist'
    ),
    path(
        'albums/<int:user_pk>/',
        views.AlbumListView.as_view(),
        name='list_artist_albums'
    ),
    path(
        'create-album/<slug:username>/',
        views.CreateAlbumView.as_view(),
        name='create_album'
    ),
    path(
        'album/<int:pk>/',
        views.AlbumView.as_view(),
        name='album_detail'
    )
]
