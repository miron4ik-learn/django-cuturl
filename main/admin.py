from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
  list_display = [ 'long_url_cut', 'short_url', 'views' ]
  
  def long_url_cut(self, obj):
    return obj.long_url[0:50]