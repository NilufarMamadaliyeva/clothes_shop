from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import SummerClothes


class UpdateClothForm(forms.ModelForm):
    class Meta:
        model = SummerClothes
        fields = ['name','description','brand','image_cloth']

    def __init__(self, *args, **kwargs):
        super(UpdateClothForm, self).__init__(*args, **kwargs)