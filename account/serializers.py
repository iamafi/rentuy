from rest_framework import serializers

from account.models import Profile, User


class ProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    phone_number = serializers.SerializerMethodField()

    def get_avatar(self, obj):
        return obj.profile.avatar.url

    def get_phone_number(self, obj):
        return obj.profile.phone_number

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'avatar', 'phone_number')
