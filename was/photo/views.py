from .forms import UploadPhotoForm
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Photo
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
            json.dumps(response),
            content_type='application/json'
        )


@login_required
def delete_photo_artist(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    photo.delete()