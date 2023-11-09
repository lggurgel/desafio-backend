import pytest
import json
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from users.models import CustomUser

@pytest.mark.django_db
@pytest.mark.parametrize(
    'data, expected_status',
    [
        (['Movie test', 2023, 'Director test', 'Action'], 201),
        (['', 2023, 'Director test', 'Action'], 400),
        (['Movie test2', '', 'Director test', 'Action'], 400),
        (['Movie test3', 2023, '', 'Action'], 400),
        (['Movie test4', 2023, 'Director test', ''], 400),
    ]
)
def test_add_movie_view_valid_and_invalid_data(data, expected_status):
    title, year, director, genre = data

    user = CustomUser.objects.create_user(
        username='testuser',
        password='testpassword'
    )

    data = {
        'title': title,
        'year': year,
        'director': director,
        'genre': genre,
        'user': user.id
    }


    client = APIClient()
    url = reverse('add-movies')
    client.login(username='testuser', password='testpassword')

    # pytest.set_trace()

    response = client.post(url, data, format='json')
    response_json = response.json()

    assert response.status_code == expected_status

@pytest.mark.django_db
@pytest.mark.parametrize(
    'data, expected_message',
    [
        (['', 2023, 'Director test', 'Action'], 'This field may not be blank.'),
        (['Movie test2', '', 'Director test', 'Action'], 'A valid integer is required.'),
        (['Movie test3', 2023, '', 'Action'], 'This field may not be blank.'),
        (['Movie test4', 2023, 'Director test', ''], 'is not a valid choice.'),
    ]
) 
def test_add_movie_view_invalid_data_messages_error(data, expected_message):
    title, year, director, genre = data

    user = CustomUser.objects.create_user(
        username='testuser',
        password='testpassword'
    )
   
    data = {
        'title': title,
        'year': year,
        'director': director,
        'genre': genre,
        'user': user.id
    }

    client = APIClient()
    url = reverse('add-movies')
    client.login(username='testuser', password='testpassword')
    
    # pytest.set_trace()

    response = client.post(url, data, format='json')

    assert expected_message in str(response.content)

