from django import forms

class form_name(forms.Form):
    name         = forms.CharField()
    email        = forms.EmailField()

    password         = forms.CharField(widget=forms.PasswordInput)
    verify_password  = forms.CharField(label="Enter your password again" , widget=forms.PasswordInput)

    text         = forms.CharField(widget = forms.Textarea)

    def clean(self):
        all_clean_data = super(form_name, self).clean()

        passwd  = all_clean_data['password']
        vpasswd = all_clean_data['verify_password']

        if (passwd!=vpasswd):
            raise forms.ValidationError("Both passwords are mis-matching")

