from django.db import models
from django.contrib.auth.models import User


class Club(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name of the group')
    users = models.ManyToManyField(User)