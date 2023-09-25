from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Tier, Image, User

class TierSerializer(ModelSerializer):
    class Meta:
        model = Tier
        fields = "__all__"

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        tier = {
            'name': obj.user.name,
            'isExpiringAllowed': obj.user.isExpiringAllowed,
        }

        return tier


class ImagesSerializer(ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'

    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        user = {
            'name': obj.user.user.name,
            'isExpiringAllowed': obj.user.user.isExpiringAllowed,
        }
        
        return user
    

   