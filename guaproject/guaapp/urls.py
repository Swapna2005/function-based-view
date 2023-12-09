from django.urls import path
from .views import RegisterForm, success_page

urlpatterns = [
    path('Register/', RegisterForm.as_view(), name='register'),
    path('success/', success_page, name='success_page'),
    # Add other URL patterns as needed
]
