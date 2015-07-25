from django.shortcuts import render
from .forms import UploadPhotoForm
from django.http import HttpResponseRedirect
from artists.models import Artists
from django.contrib.auth.decorators import login_required


@login_required
def upload_photo_artist(request):
    if request.method == 'POST':
        form = UploadPhotoForm(data=request.POST, request=request)
        if form.is_valid():
            form.clean()
            return HttpResponseRedirect('#')

    else:
        form = UploadPhotoForm()
        return render(request, 'upload_photo.html', {form: 'form'})
