from django.urls import path
from .views import deposit_money, list_people, create_person, transfer_money, update_person, delete_person, retrieve_person, withdraw_money

urlpatterns = [
    path('/', list_people, name='list_people'),
    path('/create/', create_person, name='create_person'),
    path('/<int:person_id>/update/', update_person, name='update_person'),
    path('/<int:person_id>/delete/', delete_person, name='delete_person'),
    path('/<int:person_id>/', retrieve_person, name='retrieve_person'),
    path('/<int:person_id>/deposit/', deposit_money, name='deposit_money'),
    path('/<int:person_id>/withdraw/', withdraw_money, name='withdraw_money'),
    path('/transfer/', transfer_money, name='transfer_money'),
]
