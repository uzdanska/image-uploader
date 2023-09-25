from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
# Create your models here.

NAME_TIER = {
    ('Basic', 'Basic'), 
    ('Premium', 'Premium'), 
    ('Enterprise', 'Enterprise')
}

ACCESS_LEVEL_BASIC = {
    ('200', '200')
}

ACCESS_LEVEL_PREMIUM = {
    ('200', '200'), 
    ('400', '400'), 
}

ACCESS_LEVEL_ENTERPRISE = {
    ('200', '200'), 
    ('400', '400'), 
    ('1000', '1000')
}

ACCESS_LEVEL_CHOICES = {
    'Basic': '200',
    'Premium': '400'
}


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
    name = models.CharField(max_length=100, choices=NAME_TIER, blank=False, unique=True)
    isExpiringAllowed = models.BooleanField()

    def __str__(self):
        return self.name
    

class User(models.Model):
    """
    Model representing a User.

    Each User is associated with a Tier through a foreign key relationship.

    Attributes:
        user (ForeignKey): A foreign key relationship to a Tier model representing the user's tier.
    """
    user = models.ForeignKey(Tier, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name    



class Image(models.Model):
    """
    Model representing a Image.

    Each Image is a associated with a User through a foreign key relationship.

    Attributes:
        user (ForeignKey to User): A foreign key relationship to the User model.
            This field associates the instance with a specific user.
        createdTime (DateTimeField): A field representing the date and time when the instance was created.
            It is automatically set to the current date and time when the instance is created.
        expiring_link_duration (PositiveIntegerField): A field for storing the duration of an expiring link in minutes.
            It has a default value of 0 and is validated to have a maximum value of 3000.
        image (ImageField): A field for uploading and storing images.
            The uploaded images are stored in the 'images' directory.
        access_level (CharField): A field for storing a user's access level.
            It has a maximum length of 100 characters.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=6)
    createdTime = models.DateTimeField(auto_now_add=True)
    expiring_link_duration = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(limit_value=3000)])
    image = models.ImageField(upload_to='images')
    access_level = models.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)
        if self.user.user.name == "Enterprise":
            self._meta.get_field('expiring_link_duration').default = 300
            self._meta.get_field('expiring_link_duration').validators = [MaxValueValidator(limit_value=3000)]
            self._meta.get_field('expiring_link_duration').editable = True
            self._meta.get_field('access_level').choices = ACCESS_LEVEL_ENTERPRISE
        elif self.user.user.name == "Basic":
            self._meta.get_field('expiring_link_duration').default = 0
            self._meta.get_field('expiring_link_duration').editable = False
            self._meta.get_field('access_level').choices = ACCESS_LEVEL_BASIC
        else:
            self._meta.get_field('expiring_link_duration').default = 0
            self._meta.get_field('expiring_link_duration').editable = False
            self._meta.get_field('access_level').choices = ACCESS_LEVEL_PREMIUM
    
    def save(self, *args, **kwargs):
        if self.user.user.isExpiringAllowed == False:
            self._meta.get_field('expiring_link_duration').validators = [MaxValueValidator(limit_value=3000), 
                                                                         MinValueValidator(limit_value=0)]
            if self.expiring_link_duration != 0:
                raise ValidationError("You are not allowed to have expiring_link_duration. Please set it to 0")
            if self.user.user.name == "Basic":
                for level, value in ACCESS_LEVEL_CHOICES.items():
                    if level == self.user.user.name:
                        if self.access_level != value:
                            raise ValidationError('You want to choose bigger value of image than you can. Choose smaller number :)')
            else:
                for level, value in ACCESS_LEVEL_CHOICES.items():
                    if self.access_level not in ACCESS_LEVEL_CHOICES.values():
                        raise ValidationError("You want to choose bigger value of image than you can. Choose smaller number :)")
        else:
            if not (300 <= self.expiring_link_duration <= 3000):
                raise ValidationError('You have to choose a number between 300 and 3000')
        
        super(Image, self).save(*args, **kwargs)
    

    def __str__(self):
        return f"{self.user} - {self.image}"
    
