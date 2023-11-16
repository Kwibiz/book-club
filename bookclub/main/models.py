from django.db import models

from profiles.models import Profile


class Rooms(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name of the group')
    host = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class RoomMembers(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_moderator = models.BooleanField(default=False)


class Books(models.Model):
    title = models.CharField(max_length=70, verbose_name='Book title')
    author = models.CharField(max_length=70, verbose_name='Author')
    genre = models.CharField(max_length=70, verbose_name='Genre', null=True, blank=True)
    synopsis = models.TextField(max_length=500, verbose_name='Synopsis', null=True, blank=True)
    pages = models.PositiveIntegerField(null=True, blank=True)
    room = models.OneToOneField(Rooms, on_delete=models.CASCADE)