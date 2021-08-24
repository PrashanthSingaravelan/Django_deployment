from django import forms
from django import forms
from app_1.models import users

class newuser(forms.ModelForm):
    class Meta:
        model = users
        fields = '__all__'

    def clean(self):
        all_clean_data = super(newuser,self).clean()

        fs_name = all_clean_data['first_name']
        ls_name = all_clean_data['last_name']
        em = all_clean_data['email']
