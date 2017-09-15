from django.conf.urls import url

from .views import (
    CreateArtistView,
    artist_login,
    artist_logout,
    UpdateArtistView,
    artist_delete,
    profile_page
)

urlpatterns = [
    url(r'^register/?$', CreateArtistView.as_view(), name='register_user'),
    url(r'^login/?$', artist_login, name='artist_login'),
    url(r'^logout/?$', artist_logout, name='artist_logout'),
    url(r'^update/?$', UpdateArtistView.as_view(), name='update_artist'),
    url(r'^delete/?$', artist_delete, name='delete_user'),
    url(r'^profile/?$', profile_page, name='profile_page')
]
