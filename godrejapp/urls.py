from django.urls import path
from . import views  # Import the entire views module

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contact_list, name='contact_list'),
]
