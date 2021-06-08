from rest_framework import serializers

from .models import Photo, Album


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ("id", "picture", "comment")
        read_only_fields = ("id",)

    def create(self, validated_data):
        photo = Photo(**validated_data)
        photo.artist = self.context.get("artist")
        photo.save()

        return photo


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('title', 'create_date', 'last_update')
        read_only_fields = ('created_date', 'last_update')

    def create(self, validated_data):
        album = Album(**validated_data)
        album.artist = self.context.get('artist')
        album.save()

        return album
