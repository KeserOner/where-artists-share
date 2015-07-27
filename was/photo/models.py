from django.db import models


class Photo(models.Model):
    artist = models.ForeignKey('artists.Artists')
    picture = models.ImageField(null=True, blank=True, upload_to="art_picture/")
    comment = models.TextField(max_length=500)

    def __str__(self):
        return '{}'.format(self.picture)