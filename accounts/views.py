from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm, LoginForm

class Register(CreateView):
  form_class = RegisterForm
  template_name = 'accounts/register.html'
  
  def get_success_url(self):
    return reverse_lazy('login')
  
class Login(LoginView):
  form_class = LoginForm
  template_name = 'accounts/login.html'
  
  def get_success_url(self):
    return reverse_lazy('index')
  
class Logout(LogoutView):  
  def get_next_page(self):
    return reverse_lazy('login')