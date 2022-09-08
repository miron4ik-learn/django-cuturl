from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.models import User
from .models import Link

def index(request):
  user_count = User.objects.all().count()
  link_count = Link.objects.all().count()
  views_count = Link.objects.aggregate(Sum('views'))['views__sum']
  
  return render(request, 'main/index.html', {
    'user_count': user_count,
    'link_count': link_count,
    'views_count': views_count,
  })