from django.db import models

from artists.models import Artists


class Photo(models.Model):

    artist = models.ForeignKey(Artists, on_delete=models.CASCADE, related_name="photos")

    picture = models.ImageField(
        verbose_name="Artist's picture", null=True, blank=True, upload_to="art_picture/"
    )

    comment = models.TextField(verbose_name="Comment", max_length=500)

    def __str__(self):
        return "%s" % self.picture


class Album(models.Model):

    title = models.CharField(verbose_name="Album title", max_length=255, unique=True)

    artist = models.ForeignKey(Artists, on_delete=models.CASCADE, related_name="albums")

    create_date = models.DateField(auto_now_add=True)

    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return "%s" % self.title


class AlbumPhotoRelation(models.Model):

    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
