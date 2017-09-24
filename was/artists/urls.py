from django.conf.urls import url

from .views import (
    CreateArtistAPIView,
    LoginView,
    LogoutView,
    ArtistProfileView,
    follow_artist
)

urlpatterns = [
    url(r'^register/?$', CreateArtistAPIView.as_view(), name='register_user'),
    url(r'^login/?$', LoginView.as_view(), name='artist_login'),
    url(r'^logout/?$', LogoutView.as_view(), name='artist_logout'),
    url(
        r'^update/(?P<username>[A-Za-z _-]+)/$',
        ArtistProfileView.as_view(),
        name='update_artist'
    ),
    url(
        r'^delete/(?P<username>[A-Za-z _-]+)/$',
        ArtistProfileView.as_view(),
        name='delete_user'
    ),
    url(
        r'^(?P<username>[A-Za-z _-]+)/$',
        ArtistProfileView.as_view(),
        name='profile_page'
    ),
    url(r'^follow/(?P<artist_pk>\d+)/$', follow_artist, name='follow_artist')
]
