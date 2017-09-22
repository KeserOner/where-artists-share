from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response

from .form import Artists, User
from .serializers import (
    SignupArtistSerializer,
    SigninArtistSerializer,
    ArtistSerializer
)


class CreateArtistAPIView(CreateAPIView):

    serializer_class = SignupArtistSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)


class LoginView(APIView):

    serializer_class = SigninArtistSerializer

    def post(self, request):
        serializer = SigninArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            login(request, serializer.get_user())
            return Response(status=status.HTTP_204_NO_CONTENT)


class LogoutView(APIView):

    def post(self, request):
        logout(request)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ArtistProfileView(RetrieveUpdateAPIView):

    serializer_class = ArtistSerializer
    queryset = Artists.objects.filter(user__is_active=True)
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'

    def put(self, request, **kwargs):
        error = {
            'message': 'this endpoint only accept PATCH and GET methods'
        }

        return Response(data=error, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def artist_delete(request):
    user = User.objects.get(username=request.user.username)
    user.delete()

    return HttpResponseRedirect('/')


@login_required
def follow_artist(request, **kwargs):
    artist = Artists.objects.get(user=request.user)
    artist_pk = kwargs.get('artist_pk', '')
    artist_followed = get_object_or_404(Artists, pk=artist_pk)

    if artist_followed in artist.artists_followed.all():
        artist.artists_followed.remove(artist_followed)
    else:
        artist.artists_followed.add(artist_followed)

    return HttpResponseRedirect(
        reverse(
            'profile_page',
            kwargs={'user_pk': artist_followed.user.pk}
        )
    )
