from django.conf.urls import url

from .views import (
    CreateArtistAPIView,
    LoginView,
    LogoutView,
    ArtistProfileView,
)

urlpatterns = [
    url(r'^register/?$', CreateArtistAPIView.as_view(), name='register_user'),
    url(r'^login/?$', LoginView.as_view(), name='artist_login'),
    url(r'^logout/?$', LogoutView.as_view(), name='artist_logout'),
    url(
        r'^(?P<username>[A-Za-z _-]+)/$',
        ArtistProfileView.as_view(),
        name='profile_page'
    )
]
