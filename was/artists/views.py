from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from photo.models import Photo
from photo.forms import UploadPhotoForm

from .form import UpdateArtistForm, Artists, User
from .serializers import SignupArtistSerializer, SigninArtistSerializer


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


class UpdateArtistView(UpdateView):
    template_name = 'update.html'
    form_class = UpdateArtistForm

    def get_initial(self):
        initial = {}
        user = User.objects.get(username=self.request.user.username)

        initial['username'] = user.username
        initial['email'] = user.email

        return initial

    def get_object(self):
        return get_object_or_404(Artists, user=self.request.user)

    def get_success_url(self):
        return reverse('profile_page', kwargs={'user_pk': self.object.user.pk})


class ProfilePage(DetailView):
    model = Artists
    context_object_name = 'artist'
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfilePage, self).get_context_data(**kwargs)
        photos = Photo.objects.filter(artist=self.object)
        context['photos'] = photos

        if self.request.user == self.object.user:
            context['is_user'] = True
            context['form'] = UploadPhotoForm()
        else:
            context['is_user'] = False
            # get current artist to see if he's following the artist he's
            # watching
            cur_art = Artists.objects.get(user=self.request.user)
            context['followed'] = self.object in cur_art.artists_followed.all()

        return context

    def get_object(self):
        return self.get_queryset()

    def get_queryset(self):
        user_pk = self.kwargs.get('user_pk', '')
        artist = get_object_or_404(Artists, user__pk=user_pk)

        return artist


def artist_logout(request):
    logout(request)

    return HttpResponseRedirect('/')


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
