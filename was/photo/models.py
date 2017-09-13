from django.db import models


class Photo(models.Model):
    artist = models.ForeignKey('artists.Artists')
    picture = models.ImageField(null=True, blank=True, upload_to="art_picture/")
    comment = models.TextField(max_length=500)

    def __str__(self):
        return '{}'.format(self.picture)


class Album(models.Model):
    title = models.CharField(max_length=255,
                             unique=True)
    artist = models.ForeignKey('artists.Artists')
    create_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return '%s' % self.title


class AlbumPhotoRelation(models.Model):
    photo = models.ForeignKey(Photo)
    album = models.ForeignKey(Album)

