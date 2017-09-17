from django.db import models
from django.contrib.auth.models import User


class Artists(models.Model):
    user = models.OneToOneField(User)

    artist_image = models.ImageField(
        verbose_name='Artist\'s profile image',
        null=True,
        blank=True,
        upload_to="artist_image/"
    )

    artist_banner = models.ImageField(
        verbose_name='Artist\'s banner',
        null=True,
        blank=True,
        upload_to="artist_image/"
    )

    artist_bio = models.TextField(
        max_length=500,
        verbose_name='Artist\'s biografy'
    )

    artist_signature = models.CharField(
        max_length=70,
        verbose_name='Artist\'s signature'
    )

    artist_followed = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='artists_followed',
        blank=True,
        null=True
    )

    def __str__(self):
        return 'Profil de %s' % self.user.username
