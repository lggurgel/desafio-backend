import pytest
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import CustomUser

class MoviesViewsTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.add_url = reverse('add-movies')

    @pytest.mark.django_db
    @pytest.mark.parametrize('data, expected_status', [
        (['Movie test', 2023, 'Director test', 'Action'], 201),
        (['', 2023, 'Director test', 'Action'], 400),
        (['Movie test', '', 'Director test', 'Action'], 400),
        (['Movie test', 2023, '', 'Action'], 400),
        (['Movie test', 2023, 'Director test', ''], 400),
    ])
    def test_add_movie_view_valid_data(self, data, expected_status):
        self.client.login(username='testuser', password='testpassword')

        title, year, director, genre = data

        data = {
            'title': title,
            'year': year,
            'director': director,
            'genre': genre,
            'user': self.user.id
        }
        response = self.client.post(self.add_url, data, format='json')
        assert response.status_code == expected_status
       
        # assert response.data == expected_data
        
        # self.assertDictEqual(expected_json, response.data)

    # def test_add_movie_view_invalid_title(self):
    #     self.client.login(username='testuser', password='testpassword')

    #     data = {
    #         'title': '',
    #         'year': 2023,
    #         'director': 'Test director',
    #         'genre': 'Comedy',
    #         'user': self.user.id
    #     }

    #     response = self.client.post(self.add_url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertIn('title', response.data)
    #     self.assertEqual(response.data['title'][0], 'This field may not be blank.')

    # def test_add_movie_view_invalid_year(self):
    #     self.client.login(username='testuser', password='testpassword')

    #     data = {
    #         'title': 'Filme teste 1',
    #         'year': '',
    #         'director': 'Test director',
    #         'genre': 'Comedy',
    #         'user': self.user.id
    #     }

    #     response = self.client.post(self.add_url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertIn('year', response.data)
    #     self.assertEqual(response.data['year'][0], 'A valid integer is required.')

    # def test_add_movie_view_invalid_director(self):
    #     self.client.login(username='testuser', password='testpassword')

    #     data = {
    #         'title': 'Filme teste 1',
    #         'year': 2023,
    #         'director': '',
    #         'genre': 'Comedy',
    #         'user': self.user.id
    #     }

    #     response = self.client.post(self.add_url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertIn('director', response.data)
    #     self.assertEqual(response.data['director'][0], 'This field may not be blank.')