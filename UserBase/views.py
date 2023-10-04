from django.urls import reverse
from django.views.generic import (
    CreateView, TemplateView)
from django.contrib.auth.views import PasswordResetView
from .forms import CustomUserCreationForm
from django.urls.base import reverse_lazy

class LandingView(TemplateView):
    template_name = "landing.html"

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")
    
class PasswordResetViewCustom(PasswordResetView):
        success_url = reverse_lazy("PasswordResetDoneView")

class AccountView(TemplateView):
     template_name = "UserBase/account.html"
