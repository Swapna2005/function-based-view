from django.urls import path
from .views import LoginForm, success_page

urlpatterns = [
    path('login/', LoginForm.as_view(), name='login'),
    path('success/', success_page, name='success_page'),
    # Add other URL patterns as needed
]
