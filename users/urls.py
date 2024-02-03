from django.urls import path
from .views import UserRegisterView, CustomUserLogin, LogoutView, homepage_view, profile_view, update_profile



# app_name = 'users'
urlpatterns = [
  path('signup/', UserRegisterView.as_view(), name='signup'),
  path('', CustomUserLogin.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('home/',homepage_view, name='home'),
  path('profile/',profile_view,name='profile'),
  path('update-profile/',update_profile,name='update-profile')

]