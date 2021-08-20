from django import forms
from django import forms
from app_1.models import users

class newuser(forms.ModelForm):
    class Meta:
        model = users
        fields = '__all__'