from artists.models import Artists
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.views.generic import ListView
from permissions import IsAuthenticatedAndIsOwner
from rest_framework import generics, status
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from utils import format_error

from .models import Album, AlbumPhotoRelation, Photo
from .serializers import AlbumSerializer, PhotoSerializer


class PhotoView(generics.RetrieveDestroyAPIView):

    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ListArtistPhotoView(generics.ListAPIView):

    serializer_class = PhotoSerializer

    def get_queryset(self):
        username = self.kwargs.get("username", "")
        try:
            artist = Artists.objects.get(user__username=username)
        except ObjectDoesNotExist:
            data = format_error(f"user {username} does not exist")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        return Photo.objects.filter(artist=artist)


class CreatePhotoView(generics.CreateAPIView):

    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        context = super(CreatePhotoView, self).get_serializer_context()
        username = self.kwargs.get("username", "")
        try:
            context["artist"] = Artists.objects.get(user__username=username)
        except ObjectDoesNotExist:
            data = format_error("user does not exist")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        return context


class CreateAlbumView(generics.CreateAPIView):

    serializer_class = AlbumSerializer
    permission_classes = (IsAuthenticated, IsAuthenticatedAndIsOwner)

    def get_serializer_context(self):
        context = super(CreateAlbumView, self).get_serializer_context()
        username = self.kwargs.get("username", "")
        try:
            context["artist"] = Artists.objects.get(user__username=username)
        except ObjectDoesNotExist:
            data = format_error("user does not exist")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        return context


class AlbumListView(ListView):
    model = Album
    template_name = "album_list.html"
    context_object_name = "albums"

    def get_queryset(self):
        user_pk = self.kwargs.get("user_pk", "")

        if not user_pk:
            return Http404()

        artist = Artists.objects.get(user__pk=user_pk)
        queryset = {}

        for album in Album.objects.filter(artist__pk=artist.pk):
            try:
                photo = AlbumPhotoRelation.objects.filter(album=album)[0].photo
            except IndexError:
                photo = ""
            queryset[album.title] = (photo, album.pk)

        return queryset
