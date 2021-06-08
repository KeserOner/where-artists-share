from django.urls import path

from . import views

urlpatterns = [
    path("<int:pk>/", views.PhotoView.as_view(), name="photo_detail"),
    path(
        "upload/<slug:username>/",
        views.CreatePhotoView.as_view(),
        name="upload_photo_artist",
    ),
    path(
        "list/<slug:username>/",
        views.ListArtistPhotoView.as_view(),
        name="list_photo_artist",
    ),
    path("<int:pk>/", views.AlbumView.as_view(), name="album_detail"),
    path(
        "albums/<slug:username>/",
        views.AlbumListView.as_view(),
        name="list_artist_albums",
    ),
    path(
        "create-album/<slug:username>/",
        views.CreateAlbumView.as_view(),
        name="create_album",
    ),
]
