from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests

API_BASE_URL = 'http://localhost:8000/api'  # URL da sua API

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        response = requests.post(f'{API_BASE_URL}/token/', data={'username': username, 'password': password})
        if response.status_code == 200:
            token = response.json().get('access')
            request.session['token'] = token
            return redirect('agency_list')
        return JsonResponse({'error': 'Invalid credentials'}, status=401)
    return render(request, 'login.html')

def get_api_headers(request):
    token = request.session.get('token')
    
    return {'Authorization': f'Bearer {token}'} if token else {}

def agency_list(request):
    response = requests.get(f'{API_BASE_URL}/agencies/', headers=get_api_headers(request))
    agencies = response.json()
    return render(request, 'agency_list.html', {'agencies': agencies})

def people_list(request):
    response = requests.get(f'{API_BASE_URL}/people/', headers=get_api_headers(request))
    people = response.json()
    return render(request, 'people_list.html', {'people': people})

def deposit_view(request):
    if request.method == 'POST':
        person_id = request.POST.get('person_id')
        amount = request.POST.get('amount')
        response = requests.post(f'{API_BASE_URL}/people/{person_id}/deposit/', json={'amount': amount}, headers=get_api_headers(request))
        if response.status_code == 200:
            return redirect('people_list')
    if request.method == 'GET':
        response = requests.get(f'{API_BASE_URL}/people/', headers=get_api_headers(request))
        people = response.json()
    return render(request, 'deposit.html', {'people': people})

def withdraw_view(request):
    if request.method == 'POST':
        person_id = request.POST.get('person_id')
        amount = request.POST.get('amount')
        response = requests.post(f'{API_BASE_URL}/people/{person_id}/withdraw/', json={'amount': amount}, headers=get_api_headers(request))
        if response.status_code == 200:
            return redirect('people_list')
    if request.method == 'GET':
        response = requests.get(f'{API_BASE_URL}/people/', headers=get_api_headers(request))
        people = response.json()
    return render(request, 'withdraw.html', {'people': people})

def transfer_view(request):
    if request.method == 'POST':
        from_person_id = request.POST.get('from_person_id')
        to_person_id = request.POST.get('to_person_id')
        amount = request.POST.get('amount')



        response = requests.post(f'{API_BASE_URL}/people/transfer/', json={'from_person_id': from_person_id, 'to_person_id': to_person_id, 'amount': amount}, headers=get_api_headers(request))
        if response.status_code == 200:
            return redirect('people_list')
        return JsonResponse({'error': 'Transfer failed'}, status=400)
    if request.method == 'GET':
        response = requests.get(f'{API_BASE_URL}/people/', headers=get_api_headers(request))
        people = response.json()

    return render(request, 'transfer.html', {'people': people})

def person_create(request):
    if request.method == 'POST':
        data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phone_number'),
            'agency': request.POST.get('agency_id'),
        }
        response = requests.post(f'{API_BASE_URL}/people/create/', json=data, headers=get_api_headers(request))
        if response.status_code == 201:
            return redirect('people_list')
    agencies = requests.get(f'{API_BASE_URL}/agencies/', headers=get_api_headers(request)).json()
    return render(request, 'person_create.html', {'agencies': agencies})

