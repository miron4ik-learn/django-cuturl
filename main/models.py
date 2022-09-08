from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
  class Meta:
    verbose_name = 'ссылку'
    verbose_name_plural = 'ссылки'
    
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  long_url = models.URLField(verbose_name='Длинная ссылка')
  short_url = models.CharField(verbose_name='Короткая ссылка', max_length=20)
  views = models.PositiveIntegerField(verbose_name='Переходы', default=0)