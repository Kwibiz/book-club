from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from .models import *


@login_required(login_url='profiles:login')
def create_room(request):
    if request.method == 'POST':
        user = request.user.id
        user = Profile.objects.get(user_id=user)
        name = request.POST.get('name')

        room = Rooms.objects.create(name=name, host=user)
        room_members = RoomMembers.objects.create(room=room, user=user, is_moderator=True)
        room.save()
        room_members.save()

        return redirect('profiles:profile')
    
    return render(request, 'main/create_room.html')