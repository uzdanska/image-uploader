from django.shortcuts import render
from .models import Tier, Image, User
from .serializers import TierSerializer, ImagesSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def getTiers(request):
    try:
        tiers = Tier.objects.all()
        serializer = TierSerializer(tiers, many=True)
        return Response(serializer.data)
    except Tier.DoesNotExist:
        return Response({'error': 'Tier does not found'}, status=404)
    
@api_view(['GET'])
def getTier(request, pk):
    try:
        tier = Tier.objects.get(id=pk)
        serializer = TierSerializer(tier, many=False)
        return Response(serializer.data)
    except Tier.DoesNotExist:
        return Response({'error': 'Tier with this id ' + str(pk)+ ' not found'}, status=404)
    
@api_view(['GET'])
def getUser(request, pk):
    try:
        tier = User.objects.get(id=pk)
        print(tier.user.name)
        serializer = UserSerializer(tier, many=False)
        return Response(serializer.data)
    except Tier.DoesNotExist:
        return Response({'error': 'Tier with this id ' + str(pk)+ ' not found'}, status=404)

# @api_view(['GET'])
# def getThumbNails(request):
#     try:
#         thumbNails = ThumbNail.objects.all()
#         serializer = ThumbNailsSerializer(thumbNails, many=True)
#         return Response(serializer.data)
#     except ThumbNail.DoesNotExist:
#         return Response({'error': 'ThumbNails does not found'}, status=404)

# @api_view(['GET'])
# def getThumbNail(request, pk):
#     try:
#         thumbNail = ThumbNail.objects.get(id=pk)
#         serializer = ThumbNailsSerializer(thumbNail, many=False)
#         return Response(serializer.data)
#     except ThumbNail.DoesNotExist:
#         return Response({'error': 'ThumbNail with this id ' + str(pk)+ ' not found'}, status=404)

@api_view(['GET'])
def getImages(request):
    try:
        thumbNail = Image.objects.all()
        serializer = ImagesSerializer(thumbNail, many=True)
        return Response(serializer.data)
    except Image.DoesNotExist:
        return Response({'error': 'ThumbNail with this id not found'}, status=404)
    
@api_view(['GET'])
def getUserImages(request, pk):
    try:
        user = User.objects.get(id=pk)
        images = Image.objects.filter(user=user)
        serializer = ImagesSerializer(images, many=True)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({'error': 'User with this id not found'}, status=404)
    except Image.DoesNotExist:
        return Response({'error': 'Images for this user not found'}, status=404)
    # try:
    #     # Find the user with the provided name.
    #     user = User.objects.get(name=user.user.name)  # Replace 'User' with your actual User model.

    #     # Then, filter images associated with that user.
    #     images = Image.objects.filter(user=user)

    #     # Serialize the filtered images and return the data.
    #     serializer = ImagesSerializer(images, many=True)
    #     return Response(serializer.data)
    # except User.DoesNotExist:
    #     return Response({'error': 'User with this name not found'}, status=404)
    # except Image.DoesNotExist:
    #     return Response({'error': 'Images for this user not found'}, status=404)

