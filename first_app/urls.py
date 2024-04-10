from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('first_app/', views.first_app, name='first_app'),
    path('first_app/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]