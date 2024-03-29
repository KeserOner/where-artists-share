from django.contrib.auth import login, logout

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from permissions import IsAuthenticatedAndIsOwner

from .serializers import (
    Artists,
    SignupArtistSerializer,
    SigninArtistSerializer,
    ArtistSerializer,
    ArtistListSerializer,
)


class CreateArtistAPIView(generics.CreateAPIView):

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


class ArtistProfileView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ArtistSerializer
    queryset = Artists.objects.filter(user__is_active=True)
    lookup_field = "user__username"
    lookup_url_kwarg = "username"
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthenticatedAndIsOwner)

    def put(self, request, **kwargs):
        error = {"err": "this endpoint only accept PATCH, DELETE and GET methods"}

        return Response(data=error, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ArtistListView(generics.ListAPIView):

    serializer_class = ArtistListSerializer
    queryset = Artists.objects.filter(user__is_active=True)
