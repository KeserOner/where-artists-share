from django.urls import path

from . import views

urlpatterns = [
    path(
        'register/',
        views.CreateArtistAPIView.as_view(),
        name='register_user'
    ),
    path('login/', views.LoginView.as_view(), name='artist_login'),
    path('logout/', views.LogoutView.as_view(), name='artist_logout'),
    path(
        'list-artists/',
        views.ArtistListView.as_view(),
        name='list_artists'
    ),
    path(
        '<slug:username>/',
        views.ArtistProfileView.as_view(),
        name='profile_page'
    )
]
