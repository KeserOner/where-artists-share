from django.shortcuts import render
from .forms import UploadPhotoForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Photo


@login_required
def upload_photo_artist(request):
    if request.method == 'POST':
        form = UploadPhotoForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            form.clean()
            form.save()
            return HttpResponseRedirect('/photo/upload')

    else:
        form = UploadPhotoForm()
        return render(request, 'upload_photo.html', {'form': form})

@login_required
def delete_photo_artist(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    photo.delete()