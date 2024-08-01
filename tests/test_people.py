import requests
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from agencies.models import Agency
from people.models import Person
from django.contrib.auth import get_user_model



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
def person(agency):
    return Person.objects.create(first_name="John", last_name="Doe", email="john.doe@example.com", phone_number="1234567890", agency=agency)

@pytest.fixture
def get_token(api_client, superuser):
    url = reverse('token_obtain_pair')
    response = api_client.post(url, data={'username': superuser.username, 'password': "password"})
    return response.json()['access']

@pytest.fixture
def get_header(get_token):
    return {'Authorization': f'Bearer {get_token}'}

@pytest.mark.django_db
def test_list_people(api_client, person, get_header):
    url = reverse('list_people')
    response = api_client.get(url, headers=get_header)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_create_person(api_client, agency, get_header):
    url = reverse('create_person')
    data = {
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "jane.doe@example.com",
        "phone_number": "0987654321",
        "agency": agency.id
    }
    response = api_client.post(url, data, format='json', headers=get_header)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_update_person(api_client, person, get_header):
    url = reverse('update_person', args=[person.id])
    data = {
        "first_name": "Johnny",
        "last_name": "Doe",
        "email": "johnny.doe@example.com",
        "phone_number": "0987654321",
        "agency": person.agency.id
    }
    response = api_client.put(url, data, format='json', headers=get_header)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_delete_person(api_client, person, get_header):
    url = reverse('delete_person', args=[person.id])
    response = api_client.delete(url, headers=get_header)
    assert response.status_code == status.HTTP_204_NO_CONTENT

@pytest.mark.django_db
def test_retrieve_person(api_client, person, get_header):
    url = reverse('retrieve_person', args=[person.id])
    response = api_client.get(url, headers=get_header)
    assert response.status_code == status.HTTP_200_OK
