import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from agencies.models import Agency

@pytest.fixture
def superuser():
    User = get_user_model()
    return User.objects.create_superuser(username='admin', email='admin@example.com', password='password')

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def agency():
    return Agency.objects.create(name="Test Agency", address="123 Test St", phone_number="123456789")

@pytest.fixture
def get_token(api_client, superuser):
    url = reverse('token_obtain_pair')
    response = api_client.post(url, data={'username': superuser.username, 'password': "password"})
    return response.json()['access']

@pytest.fixture
def get_header(get_token):
    return {'Authorization': f'Bearer {get_token}'}

@pytest.mark.django_db
def test_list_agencies(api_client, agency, get_header):
    url = reverse('list_agencies')
    response = api_client.get(url, headers=get_header)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_create_agency(api_client, get_header):
    url = reverse('create_agency')
    data = {
        "name": "New Agency",
        "address": "456 New St",
        "phone_number": "987654321"
    }
    response = api_client.post(url, data, format='json', headers=get_header)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_update_agency(api_client, agency, get_header):
    url = reverse('update_agency', args=[agency.id])
    data = {
        "name": "Updated Agency",
        "address": "789 Updated St",
        "phone_number": "123123123"
    }
    response = api_client.put(url, data, format='json', headers=get_header)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_delete_agency(api_client, agency, get_header):
    url = reverse('delete_agency', args=[agency.id])
    response = api_client.delete(url, headers=get_header)
    assert response.status_code == status.HTTP_204_NO_CONTENT

@pytest.mark.django_db
def test_retrieve_agency(api_client, agency, get_header):
    url = reverse('retrieve_agency', args=[agency.id])
    response = api_client.get(url, headers=get_header)
    assert response.status_code == status.HTTP_200_OK
