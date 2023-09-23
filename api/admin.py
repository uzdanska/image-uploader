from django.contrib import admin
from .models import Tier, User, Image
# Register your models here.

admin.site.register(Tier)
# admin.site.register(ThumbNail)
admin.site.register(User)
admin.site.register(Image)