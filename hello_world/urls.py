from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world_view, name='hello_world'),
    # Add more URL patterns as needed
]