from django.urls import path
from rest_framework.authtoken import views

from users.views import UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', views.obtain_auth_token),
]
