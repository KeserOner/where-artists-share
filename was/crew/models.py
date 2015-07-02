from django.db import models
from artists.models import Artists
# Create your models here.


class Crew(models.Model):
    name = models.CharField(max_length=150, primary_key=True)
    artists = models.ManyToManyField('artists.Artists')