from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='First Name')
    last_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='Last Name')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date of birth')
    location = models.CharField(max_length=30, blank=True, null=True, verbose_name='Location')
    info = models.TextField(blank=True, null=True, verbose_name='User info')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'