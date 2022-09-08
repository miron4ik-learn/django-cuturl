from django.contrib import admin
from django.urls import path, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from . import views

def anonymous_required(func, redirect_to):
  def as_view(request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect(redirect_to)
    response = func(request, *args, **kwargs)
    return response
  return as_view

urlpatterns = [
  path('register/',
      anonymous_required(views.Register.as_view(), 'profile'),
      name='register'),
  
  path('login/',
      anonymous_required(views.Login.as_view(), 'profile'),
      name='login'),
  
  path('logout/',
      login_required(views.Logout.as_view(), login_url=reverse_lazy('login')),
      name='logout'),
  
  path('profile/',
      login_required(views.profile, login_url=reverse_lazy('login')),
      name='profile'),
]