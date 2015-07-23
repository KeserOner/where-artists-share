from django.forms.models import ModelForm
from .models import Photo


class UploadPhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['picture', 'comment']

    def save(self, artist):
        photo = super(UploadPhotoForm, self).save(commit=False)
        photo.artist = artist
        photo.save()
        return photo
