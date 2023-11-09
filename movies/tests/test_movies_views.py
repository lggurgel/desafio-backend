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
        (['', 2023, 'Director test', 'Action'], [400, 'This field may not be blank.']),
        (['Movie test2', '', 'Director test', 'Action'], [400, 'A valid integer is required.']),
        (['Movie test3', 2023, '', 'Action'], [400, 'This field may not be blank.']),
        (['Movie test4', 2023, 'Director test', ''], [400, 'is not a valid choice.']),
    ]
)
def test_add_movie_view_valid_and_invalid_data_messages_error(data, expected_status):
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

    if response.status_code == 400:
        assert response.status_code == expected_status[0]
        assert expected_status[1] in str(response.content)
    else:
        assert response.status_code == expected_status
        