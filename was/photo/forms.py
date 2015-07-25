from django.forms.models import ModelForm
from .models import Photo
from artists.models import Artists

class UploadPhotoForm(ModelForm):

    class Meta:
        model = Photo
        fields = ['picture', 'comment']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(UploadPhotoForm, self).__init__(*args, **kwargs)

    def save(self):
        photo = super(UploadPhotoForm, self).save(commit=False)
        artist = Artists.objects.get(user=self.request.user)
        photo.artist = artist
        photo.save()
        return photo
