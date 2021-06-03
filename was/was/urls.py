from django.urls import include, path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.conf import settings


urlpatterns = [
    path("", include("home.urls")),
    path("admin/", admin.site.urls),
    path("artist/", include("artists.urls")),
    path("photo/", include("photo.urls")),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
