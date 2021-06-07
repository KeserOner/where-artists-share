# Generated by Django 3.2 on 2021-06-07 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='artist_banner',
            field=models.ImageField(blank=True, null=True, unique=True, upload_to='artist_banner/', verbose_name="Artist's banner"),
        ),
        migrations.AlterField(
            model_name='artists',
            name='artist_image',
            field=models.ImageField(blank=True, null=True, unique=True, upload_to='artist_image/', verbose_name="Artist's profile image"),
        ),
    ]