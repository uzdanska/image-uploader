from django.shortcuts import render
from .models import Tier, ThumbNail, Image
from .serializers import TierSerializer, ThumbNailsSerializer, ImagesSerializer
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
def getThumbNails(request):
    try:
        thumbNails = ThumbNail.objects.all()
        serializer = ThumbNailsSerializer(thumbNails, many=True)
        return Response(serializer.data)
    except ThumbNail.DoesNotExist:
        return Response({'error': 'ThumbNails does not found'}, status=404)

@api_view(['GET'])
def getThumbNail(request, pk):
    try:
        thumbNail = ThumbNail.objects.get(id=pk)
        serializer = ThumbNailsSerializer(thumbNail, many=False)
        return Response(serializer.data)
    except ThumbNail.DoesNotExist:
        return Response({'error': 'ThumbNail with this id ' + str(pk)+ ' not found'}, status=404)

@api_view(['GET'])
def getImages(request):
    try:
        thumbNail = Image.objects.all()
        serializer = ImagesSerializer(thumbNail, many=True)
        return Response(serializer.data)
    except Image.DoesNotExist:
        return Response({'error': 'ThumbNail with this id not found'}, status=404)


