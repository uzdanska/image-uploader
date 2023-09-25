from django.shortcuts import render
from .models import Tier, Image, User
from .serializers import TierSerializer, ImagesSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def getImages(request):
    """View to see all the images"""
    try:
        thumbNail = Image.objects.all()
        serializer = ImagesSerializer(thumbNail, many=True)
        return Response(serializer.data)
    except Image.DoesNotExist:
        return Response({'error': 'ThumbNail with this id not found'}, status=404)
    
@api_view(['GET'])
def getUserImages(request, userName):
    "View to see images based on user you choose 'Basic', 'Premium', 'Enterprise'"
    try: 
        tier = Tier.objects.get(name=userName)
        user = User.objects.get(user = tier)
        images = Image.objects.filter(user=user)
        serializer = ImagesSerializer(images, many=True)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({'error': 'User with this name not found'}, status=404)
    except Image.DoesNotExist:
        return Response({'error': 'Images for this user not found'}, status=404)