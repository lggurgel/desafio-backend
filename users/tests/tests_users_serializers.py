from django.test import TestCase
from rest_framework.exceptions import ValidationError
from users.models import CustomUser
from users.serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer

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

    def test_user_registration_invalid_password_serializer(self):
        invalid_data = {
            "email": "testuser@email.com",
            "password": "senha",
            "password_confirm": "senha",
        }

        serializer = UserRegistrationSerializer(data=invalid_data)

        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_user_registration_invalid_email_serializer(self):
        invalid_data = {
            "email": "email.test@.com",
            "password": "testuser@#*",
            "password_confirm": "testuser@#*",
        }

        serializer = UserRegistrationSerializer(data=invalid_data)

        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
    
    def test_user_registration_do_no_match_password(self):
        invalid_data = {
            "email": "email.teste@email.com",
            "password": "testuser@#*",
            "password_confirm": "testuser123",
        }
        serializer = UserRegistrationSerializer(data=invalid_data)
        
        with self.assertRaises(ValidationError) as context:
            serializer.is_valid(raise_exception=True)

        self.assertIn("As senhas não coicidem.", str(context.exception))

    def test_user_login_serializer(self):
        valid_data = {
            "username":"testuser@example.com",
            "password":"testuser@#*",
        }

        serializer = UserLoginSerializer(data=valid_data)

        self.assertTrue(serializer.is_valid())

    def test_user_login_invalid_password_serializer(self):
        invalid_data = {
            "username":"testuser@example.com",
            "password":"",
        }

        serializer = UserLoginSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())

    def test_valid_user_profile(self):
        data = {
            "username": "testuser",
            "email": "testuser@email.com",
            "password": "passwordtest",
            "first_name": "Test",
            "location": "Test Location",
            "favorite_filme_genre": "Action",
        }

        serializer = UserProfileSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_user_profile(self):
        data = {
            "username": "",
            "email": "invalid_email",
            "password": "key",
            "first_name": "test",
            "location": "test location",
            "favorite_film_genre": "any"
        }    

        serializer = UserProfileSerializer(data=data)
        self.assertFalse(serializer.is_valid())
    