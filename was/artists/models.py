from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Artists(models.Model):
    user = models.OneToOneField(User)
    artist_image = models.ImageField(null=True, blank=True, upload_to="/artist_image/")


    def __str__(self):
        return 'Profil de {0}'.format(self.username)

