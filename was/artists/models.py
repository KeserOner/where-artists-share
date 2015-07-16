from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class Artists(models.Model):
    user = models.OneToOneField(User)
    artist_image = models.ImageField(null=True, blank=True, upload_to="/artist_image/")
    artist_banner = models.ImageField(null=True, blank=True, upload_to="/artist_image")
    artist_bio = models.TextField(max_length=500)
    artist_signature = models.CharField(max_length=70)

    def __str__(self):
        return 'Profil de {0}'.format(self.user.username)
