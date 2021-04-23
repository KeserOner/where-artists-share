from django.urls import path

from . import views

urlpatterns = [
    path(
        'register/',
        views.CreateArtistAPIView.as_view(),
        name='artist_register'
    ),
    path('login/', views.LoginView.as_view(), name='artist_login'),
    path('logout/', views.LogoutView.as_view(), name='artist_logout'),
    path(
        'list-artists/',
        views.ArtistListView.as_view(),
        name='artists_list'
    ),
    path(
        '<slug:username>/',
        views.ArtistProfileView.as_view(),
        name='artist_detail'
    )
]
