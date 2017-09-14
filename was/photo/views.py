from .forms import UploadPhotoForm
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from artists.models import Artists
from .models import Photo, Album, AlbumPhotoRelation
import json


@login_required
@require_POST
def upload_photo_artist(request):
    form = UploadPhotoForm(request.POST, request.FILES, request=request)
    if form.is_valid():
        form.clean()
        form.save()
        response = {
            'code': 1,
            'message': 'success',
        }
        return HttpResponse(
            json.dumps(response),
            content_type='application/json'
        )
    else:
        response = form.errors.as_json()
        return HttpResponse(
            response,
            content_type='application/json'
        )


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
