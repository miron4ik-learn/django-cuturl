from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm, LoginForm, AddLinkForm
from main.models import Link
from .utils import generate_short_url

def profile(request):
  success = False
  form = None
  
  if request.GET.get('act') == 'new':
    form = AddLinkForm(request.POST)
    
    if form.is_valid():
      link = form.save(commit=False)
      link.user = request.user
      link.short_url = generate_short_url()
      
      link.save()
      success = True
  
  links = Link.objects.filter(user=request.user.id)
  
  return render(request, 'accounts/profile.html', {
    'links': links,
    'success': success,
    'form': form,
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