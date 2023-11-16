from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('create-room', views.create_room, name='create_room')
]