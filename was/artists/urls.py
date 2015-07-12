from django.conf.urls import url
from .views import CreateArtistView, artist_login

urlpatterns = [
    url(r'^register/', CreateArtistView.as_view(), name='register_user'),
    url(r'^login/', artist_login, name='artist_login')
]