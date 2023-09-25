from django.test import TestCase
import os
from api.models import Tier, User, Image
from django.core.exceptions import ValidationError


class TierModelTestCase(TestCase):
    def setUp(self):
        Tier.objects.create(name='Basic', isExpiringAllowed=False)
        Tier.objects.create(name='Premium', isExpiringAllowed=False)
        Tier.objects.create(name="Enterprise", isExpiringAllowed=True)

    def test_tier_str_method(self):
        """Test the __str__() method of Tier model."""
        basic_tier = Tier.objects.get(name='Basic')
        premium_tier = Tier.objects.get(name='Premium')
        enterprise_tier = Tier.objects.get(name='Enterprise')

        self.assertEqual(str(basic_tier), 'Basic')
        self.assertEqual(str(premium_tier), 'Premium')
        self.assertEqual(str(enterprise_tier), 'Enterprise')

    def test_tier_is_expiring_allowed(self):
        """Test the isExpiringAllowed attribute of Tier model."""
        basic_tier = Tier.objects.get(name='Basic')
        premium_tier = Tier.objects.get(name='Premium')
        enterprise_tier = Tier.objects.get(name='Enterprise')

        self.assertFalse(basic_tier.isExpiringAllowed)
        self.assertFalse(premium_tier.isExpiringAllowed)
        self.assertTrue(enterprise_tier.isExpiringAllowed)

class UserModelTestCase(TestCase):
    def setUp(self):
        basicTier = Tier.objects.create(name="Basic", isExpiringAllowed=False)
        self.userBasic = User.objects.create(user=basicTier)
    
    def test_user_str_method(self):
        expected_str = "Basic"
        self.assertEqual(str(self.userBasic), expected_str)

    def test_user_creation(self):
        self.assertIsInstance(self.userBasic, User)

    def test_user_tier_relationship(self):
        tierUser = self.userBasic.user
        self.assertEqual(tierUser.name, 'Basic')
        self.assertFalse(tierUser.isExpiringAllowed)


class ImageModelTestCase(TestCase):
    def setUp(self):
        basicTier = Tier.objects.create(name="Basic", isExpiringAllowed=False)
        enterpriseTier = Tier.objects.create(user="Enterprise", isExpiringAllowed=True)

        userBasic = User.objects.create(user=basicTier)
        userEnterprise = User.objects.create(user=enterpriseTier)

        self.basic_image = Image.objects.create(user=userBasic, expiring_link_duration = 0, image="/test/Borobudur-complete.jpg", access_level='200')
        self.enterprise_image = Image.objects.create(user=userEnterprise,  expiring_link_duration = 400, image="/test/Borobudur-complete.jpg", access_level='400')

        self.list_access_level_basic = [('200', '200')]
        self.list_access_level_enterprise = [('200', '200'), ('400', '400'), ('1000', '1000')]
        

    def test_image_creation(self):
        """Test the creation of an Image instance."""
        self.assertIsInstance(self.basic_image, Image)
        self.assertIsInstance(self.enterprise_image, Image)

    def test_default_expiring_link_duration(self):
        """Test the default expiring_link_duration based on user's tier."""
        self.assertEqual(self.basic_image.expiring_link_duration, 0)
        self.assertEqual(self.enterprise_image.expiring_link_duration, 400)

    def test_expiring_link_duration_validation(self):
        """Test the validation of expiring_link_duration."""
        with self.assertRaises(ValidationError):
            self.basic_image.expiring_link_duration = 5000
            self.basic_image.save()

        with self.assertRaises(ValidationError):
            self.enterprise_image.expiring_link_duration = -1000
            self.enterprise_image.save()

    def test_access_level_choices(self):
        """Test access_level choices based on user's tier."""
        self.assertEqual(self.basic_image.access_level, self.list_access_level_basic[0][0])
        self.assertEqual(self.enterprise_image.access_level, self.list_access_level_enterprise[1][0])

        
    def test_access_level_validation(self):
        """Test access_level validation based on user's tier."""
        with self.assertRaises(ValidationError):
            self.basic_image.access_level = "1000"
            self.basic_image.save()
