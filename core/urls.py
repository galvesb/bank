
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/agencies", include("agencies.urls")),
    path('api/people', include('people.urls')),
]
