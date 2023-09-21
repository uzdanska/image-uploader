from django.urls import path
from . import views

urlpatterns = [
    path('tiers/', views.getTiers, name='tiers'),
    path('tiers/<str:pk>', views.getTier, name="tier"),
    path('thumbnails/', views.getThumbNails, name='thumbnails'),
    path('thumbnails/<str:pk>', views.getThumbNail, name="thumbnail"),
    path('images/', views.getImages, name='images'),
]