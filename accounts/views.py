from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm, LoginForm
from main.models import Link

def profile(request):
  links = Link.objects.filter(user=request.user.id)
  print()
  
  return render(request, 'accounts/profile.html', {
    'links': links,
  })

class Register(CreateView):
  form_class = RegisterForm
  template_name = 'accounts/register.html'
  
  def get_success_url(self):
    return reverse_lazy('login')
  
class Login(LoginView):
  form_class = LoginForm
  template_name = 'accounts/login.html'
  
  def get_success_url(self):
    return reverse_lazy('profile')
  
class Logout(LogoutView):  
  def get_next_page(self):
    return reverse_lazy('login')