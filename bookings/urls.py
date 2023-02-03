from django.contrib import admin
from django.urls import path
from .views import index_view, register_view, login_view, resetpassword_view, contact_view, reservations_view, menu_view


urlpatterns = [
    path('', index_view, name='index'),
    path('register', register_view, name='register'),
    path('login', login_view, name='login'),
    path('resetpassword', resetpassword_view, name='resetpassword'),
    path('contact', contact_view, name='contact'),
    path('reservations', reservations_view, name='reservations'),
    path('menu', menu_view, name='menu'),
]
