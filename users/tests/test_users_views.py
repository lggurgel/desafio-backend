from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import CustomUser

class UserViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.login_url = reverse('login') 
        self.logout_url = reverse('logout')
        self.profile_url = reverse('profile')

        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='testuser@#*'
        )

    def test_user_registration_valid_data(self):
        data = {
            'email': 'testuser@example.com',
            'password': 'testuser@#*',
            'password_confirm': 'testuser@#*',
        }

        response = self.client.post(self.register_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('user', response.data)
        self.assertIn('message', response.data)
        self.assertEqual(response.data["message"], "User registered successfully")

    def test_user_registration_invalid_data(self):
        invalid_data = {
            'email': 'testuser@.com',
            'password': 'testuser@#*',
            'password_confirm': 'testuser',
        }

        response = self.client.post(self.register_url, invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_user_registration_password_do_not_match(self):
        data = {
            'email': 'testpassword@email.com',
            'password': 'password123',
            'password_confirm': 'password12',
        }
        response = self.client.post(self.register_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_login_valid_data(self):
        data = {
            'username': 'testuser',
            'password': 'testuser@#*'
        } 

        response = self.client.post(self.login_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], "Login successfully.")

    def test_user_login_invalid_user(self):
        data = {
            'username': 'invaliduser',
            'password': 'password',
        }

        response = self.client.post(self.login_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'Invalid credentials.')

    def test_user_login_invalid_password(self):
        data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }

        response = self.client.post(self.login_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'Invalid credentials.')

    def test_user_logout(self):
        self.client.login(username='testuser', password='testuser@#*')

        response = self.client.get(self.logout_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'Logout successfully completed.')

    def test_get_user_profile(self):
        self.client.login(username='testuser', password='testuser@#*')

        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user_data = response.json()
        self.assertEqual(user_data['username'], 'testuser')
        self.assertEqual(user_data['email'], 'testuser@email.com')
        self.assertEqual(user_data['first_name'], '')
        self.assertEqual(user_data['location'], '')
        self.assertEqual(user_data['favorite_film_genre'], 'Select Genre')

    def test_patch_user_profile(self):
        self.client.login(username='testuser', password='testuser@#*')

        data = {
            'first_name': 'Teste',
            'location': 'Brasil',
            'favorite_film_genre': 'Science Fiction'
        }

        response = self.client.patch(self.profile_url, data=data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        user_data = response.json()
        # self.assertEqual(user_data['username'], 'testuser')
        # self.assertEqual(user_data['email'], 'testuser@email.com')
        self.assertEqual(user_data['first_name'], 'Teste')
        self.assertEqual(user_data['location'], 'Brasil')
        self.assertEqual(user_data['favorite_film_genre'], 'Science Fiction')