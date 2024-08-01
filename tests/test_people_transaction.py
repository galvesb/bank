import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

from agencies.models import Agency
from people.models import Person

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
def test_deposit_money(api_client, person, get_header):
    url = reverse('deposit_money', args=[person.id])
    data = {"amount": 100.0}
    response = api_client.post(url, data, format='json', headers=get_header)

    person.refresh_from_db()

    assert response.status_code == status.HTTP_200_OK
    assert person.balance == 100.0

@pytest.mark.django_db
def test_withdraw_money(api_client, person, get_header):
    person.balance = 100.0
    person.save()
    url = reverse('withdraw_money', args=[person.id])
    data = {"amount": 50.0}
    response = api_client.post(url, data, format='json', headers=get_header)

    person.refresh_from_db()

    assert response.status_code == status.HTTP_200_OK
    assert person.balance == 50.0

@pytest.mark.django_db
def test_transfer_money(api_client, person, agency, get_header):
    person.balance = 100.0
    person.save()
    recipient = Person.objects.create(first_name="Jane", last_name="Doe", email="jane.doe@example.com", phone_number="0987654321", agency=agency)
    url = reverse('transfer_money')
    data = {
        "from_person_id": person.id,
        "to_person_id": recipient.id,
        "amount": 50.0
    }
    response = api_client.post(url, data, format='json', headers=get_header)
    assert response.status_code == status.HTTP_200_OK
    person.refresh_from_db()
    recipient.refresh_from_db()
    assert person.balance == 50.0
    assert recipient.balance == 50.0
