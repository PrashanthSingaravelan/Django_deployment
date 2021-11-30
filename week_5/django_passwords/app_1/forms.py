from django import forms
from django.contrib.auth.models import User
from app_1.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username' , 'email' , 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site' , 'profile_pic')

# Take ('username' , 'email' , 'password') fields from the User model and place in the data-base
# Take ('portfolio_site' , 'profile_pic') fields from the UserProfileInfo model and place in the data-base

