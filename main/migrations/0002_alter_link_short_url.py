# Generated by Django 4.0.5 on 2022-09-08 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='short_url',
            field=models.CharField(max_length=20, unique=True, verbose_name='Короткая ссылка'),
        ),
    ]