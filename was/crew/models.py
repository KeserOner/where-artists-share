from django.db import models

from artists.models import Artists


class Crew(models.Model):

    name = models.CharField(
        verbose_name='Crew',
        max_length=150,
        unique=True
    )

    artists = models.ManyToManyField(Artists)

    def __str__(self):
        return 'Crew %s' % self.name
