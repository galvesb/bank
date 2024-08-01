from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('agencies/', views.agency_list, name='agency_list'),
    path('people/', views.people_list, name='people_list'),
    path('people/create/', views.person_create, name='person_create'),
    path('deposit/', views.deposit_view, name='deposit'),
    path('withdraw/', views.withdraw_view, name='withdraw'),
    path('transfer/', views.transfer_view, name='transfer'),
]
