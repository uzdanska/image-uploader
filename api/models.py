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
    isExpiringAllowed = models.BooleanField()

    def __str__(self):
        return self.name
    


ACCESS_LEVEL_CHOICES = {
    'Basic': [('basic', '200')],
    'Premium': [('premium', '400'), ('basic', '200')],
    'Enterprise': [('enterprise', '1000'), ('premium', '400'), ('basic', '200')],
}

ACCESS_LEVEL_BASIC = {
    'Basic': '200'
}

class User(models.Model):
    user = models.ForeignKey(Tier, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name    



class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    createdTime = models.DateTimeField(auto_now_add=True)
    expiring_link_duration = models.PositiveIntegerField(default=300)
    image = models.ImageField(upload_to='images')
    access_level = models.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)
        if self.user.user.name == "Enterprise":
            self._meta.get_field('expiring_link_duration').default = 300
            self._meta.get_field('expiring_link_duration').validators = [MaxValueValidator(limit_value=1000), 
                                                                         MinValueValidator(limit_value=300)]
            self._meta.get_field('expiring_link_duration').editable = True
        else:
            self._meta.get_field('expiring_link_duration').default = 0
            self._meta.get_field('expiring_link_duration').editable = False
    
    def save(self, *args, **kwargs):
        if self.user.user.name not in ACCESS_LEVEL_CHOICES:
            raise ValidationError("Invalid user name")

        allowed_choices = ACCESS_LEVEL_CHOICES[self.user.user.name]
        valid_access_levels = dict(allowed_choices).keys()
        
        if self.access_level not in valid_access_levels:
            raise ValidationError("Invalid access level for this user")

        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} - {self.image} + {self.access_level}"
    
