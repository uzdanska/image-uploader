from django.urls import path
from . import views

urlpatterns = [
    path('images/', views.getImages, name='images'),
    path('images/user/<str:userName>', views.getUserImages, name='Userimages'),
]