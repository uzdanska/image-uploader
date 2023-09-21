from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import ThumbNail, Tier, Image

class TierSerializer(ModelSerializer):
    class Meta:
        model = Tier
        fields = "__all__"

class ThumbNailsSerializer(ModelSerializer):

    class Meta:
        model = ThumbNail
        fields = '__all__'

    tier = serializers.SerializerMethodField()
    def get_tier(self, obj):
        return {
            'name': obj.tier.name,
            'isOriginalAllow': obj.tier.isOrginalAllowed,
            'isExpiringAllowed': obj.tier.isExpiringAllowed
        }
    
class ImagesSerializer(ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'

    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        thumbnail = ThumbNail.objects.get(tier=obj.user.tier)
        thumbnailData = {
            'minHeight': thumbnail.minHeight,
            'maxHeight': thumbnail.maxHeight
        }
        user = {
            'name': obj.user.tier.name,
            'isOriginalAllow': obj.user.tier.isOrginalAllowed,
            'isExpiringAllowed': obj.user.tier.isExpiringAllowed
        }
        return {
            'tier': user, 
            'thumbnail': thumbnailData
        }
    

   