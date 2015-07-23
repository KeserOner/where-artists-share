from django.shortcuts import render
from .forms import UploadPhotoForm
from django.http import HttpResponseRedirect
from artists.models import Artists

def upload_photo_artist(request):
    if request.method == 'POST':
        form = UploadPhotoForm(data=request.POST)
        if form.is_valid():
            artist = Artists.objects.get(user=request.user)
            form.clean()
            form.save(artist)
            return HttpResponseRedirect('#')

    else:
        form = UploadPhotoForm()
        return render(request, 'upload_photo.html', {form: 'form'})
