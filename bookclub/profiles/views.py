from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


@login_required(login_url='profiles:login')
def profile(request):
    user_username = request.user.username
    return render(request, 'profiles/profile.html', context={'user': user_username})

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            user_instance = request.user
            profile = Profile.objects.create(user=user_instance)
            profile.save()

            return redirect('profiles:profile')
    
    else:
        form = UserCreationForm()

    return render(request, 'profiles/sign_up.html', context={'form': form,})


class LogoutUserView(LogoutView):
    next_page = 'profiles:profile'
    

class LoginUserView(LoginView):
    template_name = 'profiles/login.html'
    next_page = 'profiles:profile'
    redirect_authenticated_user = True