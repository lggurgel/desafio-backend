from django.test import TestCase
from users.models import CustomUser

class CustomUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create(username='testuser', email='testuser@email.com')

    def test_str_representation(self):
        user = CustomUser.objects.get(id=self.user.id)
        self.assertEqual(str(user), user.username)