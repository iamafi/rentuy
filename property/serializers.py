from rest_framework import serializers

from account.serializers import ProfileSerializer
from property.models import Property, PropertyImage, Review, PropertyRequest


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ('image',)


class PropertyListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return obj.images.first().image.url

    class Meta:
        model = Property
        fields = ('id', 'title', 'price', 'image',)


class PropertyDetailSerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    owner = ProfileSerializer()

    class Meta:
        model = Property
        fields = ('id', 'title', 'images', 'rating', 'owner', 'pets', 'long_term', 'rooms', 'for_family', 'description',
                  'address', 'price')


class ReviewSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()

    class Meta:
        model = Review
        fields = ('user', 'rating', 'comment', 'created')


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyRequest
        fields = '__all__'
