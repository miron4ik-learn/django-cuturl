from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
  username = forms.CharField()
  password1 = forms.CharField()
  password2 = forms.CharField()
  
  class Meta:
    model = User
    fields = [ 'username', 'password1', 'password2' ]
    
class LoginForm(AuthenticationForm):
  username = forms.CharField()
  password = forms.CharField()