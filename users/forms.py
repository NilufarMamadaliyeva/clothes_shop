from django import forms
from .models import Customer
from django.contrib.auth.forms import UserCreationForm

class CustomerCreateForm(UserCreationForm):
  class Meta:
    model = Customer
    fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
    

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('username', 'first_name', 'last_name', 'email','user_image','phone')


        