from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('signup/', views.sign_up, name='sign_up'),
    path('profile/', views.profile, name='profile'),
]