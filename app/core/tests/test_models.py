from django.test import TestCase
from django.contrib.auth import get_user_model


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
