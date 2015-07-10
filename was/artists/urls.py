from django.conf.urls import url
from .views import CreateArtistView

urlpatterns = [
    url(r'^register/', CreateArtistView.as_view(), name='register_user'),
]