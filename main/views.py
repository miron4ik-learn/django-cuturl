from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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
  
def redirect(request, short_url):
  link = get_object_or_404(Link, short_url=short_url)
  link.views += 1
  link.save()
  return HttpResponseRedirect(link.long_url)