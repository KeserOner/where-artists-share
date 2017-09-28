from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView
)

from artists.models import Artists
from utils import format_error

from .serializers import PhotoSerializer
from .forms import UploadPhotoForm, CreateAlbumForm
from .models import Photo, Album, AlbumPhotoRelation


class PhotoView(RetrieveAPIView):

    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()


class CreatePhotoView(CreateAPIView):

    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        context = super(CreatePhotoView, self).get_serializer_context()
        username = self.kwargs.get('username', '')
        try:
            context['artist'] = Artists.objects.get(user__username=username)
        except ObjectDoesNotExist:
            data = format_error('user does not exist')
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        return context


@login_required
def delete_photo_artist(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    photo.delete()


class AlbumListView(ListView):
    model = Album
    template_name = 'album_list.html'
    context_object_name = 'albums'

    def get_queryset(self):
        user_pk = self.kwargs.get('user_pk', '')

        if not user_pk:
            return Http404()

        artist = Artists.objects.get(user__pk=user_pk)
        queryset = {}

        for album in Album.objects.filter(artist__pk=artist.pk):
            try:
                photo = AlbumPhotoRelation.objects.filter(album=album)[0].photo
            except IndexError:
                photo = ''
            queryset[album.title] = (photo, album.pk)

        return queryset


class CreateAlbumView(CreateView):

    model = Album
    form_class = CreateAlbumForm
    template_name = 'create_album.html'

    def get_form_kwargs(self):
        kwargs = super(CreateAlbumView, self).get_form_kwargs()
        kwargs.update({'request': self.request})

        return kwargs

    def get_success_url(self):
        user_pk = self.request.user.pk
        return reverse('list_artist_albums', kwargs={'user_pk': user_pk})


class AlbumView(DetailView):

    model = Album
    context_object_name = 'album'
    template_name = 'album_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumView, self).get_context_data(**kwargs)
        ids = AlbumPhotoRelation.objects.values_list(
            'photo_id',
            flat=True).filter(album=self.object)
        photos = Photo.objects.filter(pk__in=set(ids))
        context['photos'] = photos
        context['form'] = UploadPhotoForm()
        return context
