from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class TestModelUser(TestCase):

    def test_create_user_success(self):
        email = 'test@gmail.com'
        password = 'Test@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_user_email(self):
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='Test@123'
        )

        self.assertEqual(user.email, email.lower())

    def test_user_with_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test@123')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            email='test@gmail.com',
            password='Test@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)
