from django.urls import path
from .views import atm_menu  # Make sure this is the correct view

urlpatterns = [
    path('', atm_menu, name='atm_menu'),  # This maps to the root of the ATM app
]
