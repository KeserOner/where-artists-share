from django.forms.models import ModelForm
from .models import Photo, Album, AlbumPhotoRelation
from artists.models import Artists


class UploadPhotoForm(ModelForm):

    class Meta:
        model = Photo
        fields = ['picture', 'comment']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(UploadPhotoForm, self).__init__(*args, **kwargs)

    def save(self):
        photo = super(UploadPhotoForm, self).save(commit=False)
        artist = Artists.objects.get(user=self.request.user)
        photo.artist = artist
        photo.save()
        if 'album_pk' in self.data:
            album = Album.objects.get(pk=self.data['album_pk'])
            AlbumPhotoRelation.objects.create(
                photo=photo,
                album=album
            )
        return photo


class CreateAlbumForm(ModelForm):

    class Meta:
        model = Album
        fields = ['title']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CreateAlbumForm, self).__init__(*args, **kwargs)

    def save(self):
        album = super(CreateAlbumForm, self).save(commit=False)
        artist = Artists.objects.get(user=self.request.user)
        album.artist = artist
        album.save()

        return album
