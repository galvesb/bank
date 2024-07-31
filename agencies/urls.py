from django.urls import path
from .views import list_agencies, create_agency, update_agency, delete_agency, retrieve_agency

urlpatterns = [
    path('/', list_agencies, name='list_agencies'),
    path('/create/', create_agency, name='create_agency'),
    path('/<int:agency_id>/update/', update_agency, name='update_agency'),
    path('/<int:agency_id>/delete/', delete_agency, name='delete_agency'),
    path('/<int:agency_id>/', retrieve_agency, name='retrieve_agency'),
]
