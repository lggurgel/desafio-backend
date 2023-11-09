import pytest
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
        (['Movie test', '', 'Director test', 'Action'], 400),
        (['Movie test', 2023, '', 'Action'], 400),
        (['Movie test', 2023, 'Director test', ''], 400),
    ]
)
def test_add_movie_view_valid_data(data, expected_status):
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

    assert response.status_code == expected_status