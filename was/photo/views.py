from artists.models import Artists
from django.core.exceptions import ObjectDoesNotExist
from permissions import IsAuthenticatedAndIsOwner
from rest_framework import generics, status
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from utils import format_error

from . import models, serializers


class PhotoView(generics.RetrieveDestroyAPIView):

    serializer_class = serializers.PhotoSerializer
    queryset = models.Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ListArtistPhotoView(generics.ListAPIView):

    serializer_class = serializers.PhotoSerializer

    def get_queryset(self):
        username = self.kwargs.get("username", "")
        try:
            artist = Artists.objects.get(user__username=username)
        except ObjectDoesNotExist:
            data = format_error(f"user {username} does not exist")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        return models.Photo.objects.filter(artist=artist)


class CreatePhotoView(generics.CreateAPIView):

    serializer_class = serializers.PhotoSerializer
    queryset = models.Photo.objects.all()
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


class AlbumView(generics.RetrieveDestroyAPIView):

    serializer_class = serializers.AlbumSerializer()
    queryset = models.Album.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CreateAlbumView(generics.CreateAPIView):

    serializer_class = serializers.AlbumSerializer
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


class ListAlbumiew(generics.ListAPIView):

    serializer_class = serializers.AlbumSerializer

    def get_queryset(self):
        username = self.kwargs.get("username", "")
        try:
            artist = Artists.objects.get(user__username=username)
        except ObjectDoesNotExist:
            data = format_error(f"user {username} does not exist")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        return models.Album.objects.filter(artist=artist)
