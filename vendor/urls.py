from django.urls import path, include
from rest import urls

urlpatterns = [
    path('', include(urls))
]