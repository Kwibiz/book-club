# Generated by Django 4.2.7 on 2023-11-10 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=20, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(blank=True, verbose_name='Date of birth')),
                ('location', models.CharField(blank=True, max_length=30, verbose_name='Location')),
                ('info', models.TextField(blank=True, verbose_name='User info')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
