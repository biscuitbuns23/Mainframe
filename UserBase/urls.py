from django.contrib import admin
from django.urls import path
from .views import SignupView
from django.contrib.auth.views import LoginView

app_name = "UserBase"

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login')
]