from django.contrib import admin
from django.urls import path, include
from atm.views import atm_menu  # Import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', atm_menu, name='atm_menu'),  # Redirect root to atm_menu
    path('atm/', include('atm.urls')),  # Ensure this is included
]
