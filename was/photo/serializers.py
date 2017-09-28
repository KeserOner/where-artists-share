from rest_framework import serializers

from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('id', 'picture', 'comment')
        read_only_fields = ('id',)

    def create(self, validated_data):
        photo = Photo(**validated_data)
        photo.artist = self.context.get('artist')
        photo.save()

        return photo
