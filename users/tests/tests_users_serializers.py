from django.test import TestCase
from rest_framework.exceptions import ValidationError
from users.models import CustomUser
from users.serializers import UserRegistrationSerializer

class UserSerializerTest(TestCase):
    def test_user_registration_serializer(self):
        valid_data = {
            "email": "testuser@email.com",
            "password": "testuser@#*",
            "password_confirm": "testuser@#*",
        }

        serializer = UserRegistrationSerializer(data=valid_data)

        self.assertTrue(serializer.is_valid())

        user = serializer.create(valid_data)

        self.assertEqual(user.email, valid_data["email"])
        self.assertTrue(user.check_password(valid_data["password"]))

        invalid_data = {
            "email": "testuser@email.com",
            "password": "senha",
            "password_confirm": "senha",
        }

        serializer = UserRegistrationSerializer(data=invalid_data)

        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)