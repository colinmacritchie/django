from django import forms
from django.forms import extras
from .models import SignUp


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        #if not extension == "gmail":    #Change this to whatever.
            #raise forms.ValidationError("Please use a valid gmail email address") #Change message here.
        return email
