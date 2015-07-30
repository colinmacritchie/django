from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    #Delete this validation if you want to accept all email types.
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if not extension == "gmail":    #Change this to whatever.
            raise forms.ValidationError("Please use a valud gmail email address") #Change message here.
        return email
