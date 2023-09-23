from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Tier, Image, User, ACCESS_LEVEL_CHOICES

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

# class ThumbNailsSerializer(ModelSerializer):

#     class Meta:
#         model = ThumbNail
#         fields = '__all__'

#     tier = serializers.SerializerMethodField()
#     def get_tier(self, obj):
#         return {
#             'name': obj.tier.name,
#             'isOriginalAllow': obj.tier.isOrginalAllowed,
#             'isExpiringAllowed': obj.tier.isExpiringAllowed
#         }
    
class ImagesSerializer(ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'

    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        user = {
            'name': obj.user.user.name,
            'isExpiringAllowed': obj.user.user.isExpiringAllowed,
            'access_level_choices': [],
        }

        if obj.user.user.name in ACCESS_LEVEL_CHOICES:
            allowed_choices = ACCESS_LEVEL_CHOICES[obj.user.user.name]
            user['access_level_choices'] = [{'user': choice[0], 'value': choice[1]} for choice in allowed_choices]

        return user
    

   