from django.conf.urls import url

from .views import (
    CreateArtistAPIView,
    LoginView,
    artist_logout,
    UpdateArtistView,
    artist_delete,
    ProfilePage,
    follow_artist
)

urlpatterns = [
    url(r'^register/?$', CreateArtistAPIView.as_view(), name='register_user'),
    url(r'^login/?$', LoginView.as_view(), name='artist_login'),
    url(r'^logout/?$', artist_logout, name='artist_logout'),
    url(r'^update/?$', UpdateArtistView.as_view(), name='update_artist'),
    url(r'^delete/?$', artist_delete, name='delete_user'),
    url(
        r'^profile/(?P<user_pk>\d+)/$',
        ProfilePage.as_view(),
        name='profile_page'),
    url(r'^follow/(?P<artist_pk>\d+)/$', follow_artist, name='follow_artist')
]
