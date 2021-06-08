from django.contrib.auth.models import User
from django.db import models
from django.dispatch.dispatcher import receiver


class Artists(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    artist_image = models.ImageField(
        verbose_name="Artist's profile image",
        null=True,
        blank=True,
        unique=True,
        upload_to="artist_image/",
    )

    artist_banner = models.ImageField(
        verbose_name="Artist's banner",
        unique=True,
        null=True,
        blank=True,
        upload_to="artist_banner/",
    )

    artist_bio = models.TextField(max_length=500, verbose_name="Artist's biografy")

    artist_signature = models.CharField(
        max_length=70, verbose_name="Artist's signature"
    )

    artist_followed = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="artists_followed",
        blank=True,
        null=True,
    )

    def __str__(self):
        return "Profil de %s" % self.user.username


@receiver(models.signals.pre_delete, sender=Artists)
def delete_images(sender, instance, **kwargs):
    if instance.artist_image:
        instance.artist_image.delete(False)
    if instance.artist_banner:
        instance.artist_banner.delete(False)
