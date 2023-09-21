from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Tier(models.Model):
    """
         Model representing user account tiers.
    
        Each tier can have a unique name and can specify whether users are allowed
        to view the original image and set expiration times for links.

        Attributes:
            name (str): Name of tiers.
            isOrginalAllowed (bool): Tells us whether users can view the original image or not.
            isExpiringAllowed (bool): Tells us whether users can set expiration times for links or not.

        Methods:
            __str__(): Returns the name of the tier as its string representation.


    """
    name = models.CharField(max_length=100, blank=False, unique=True)
    isOrginalAllowed = models.BooleanField()
    isExpiringAllowed = models.BooleanField()

    def __str__(self):
        return self.name
    

class ThumbNail(models.Model):
    """
         Model representing user account tiers.
    
        Each tier can have a unique name and can specify whether users are allowed
        to view the original image and set expiration times for links.

        Attributes:
            name (str): Name of tiers.
            isOrginalAllowed (bool): Tells us whether users can view the original image or not.
            isExpiringAllowed (bool): Tells us whether users can set expiration times for links or not.

        Methods:
            __str__(): Returns the name of the tier as its string representation.


    """
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE, help_text="Selected tier associated with this user account.")
    minHeight = models.IntegerField(default=200,
        validators=[
            MaxValueValidator(200),
            MinValueValidator(200)
        ],
        help_text="Stores the minimum possible value of the image")
    maxHeight = models.IntegerField(
        validators=[
            MaxValueValidator(1000),
            MinValueValidator(200)
        ],
        help_text="Stores the maximum possible value of the image")
    

    def __str__(self):
        return f"{self.tier} - max height of the image is {self.maxHeight}px"
    

class User(models.Model):
    tier = models.ForeignKey(Tier, on_delete=models.PROTECT)

    def __str__(self):
        return self.tier.name
    

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    createdTime = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')

    # thumbnail = models.ForeignKey(ThumbNail, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.image}"
    