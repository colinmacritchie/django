from django import forms
from django.forms import extras
from .models import SignUp, ApplicationNew


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
        if not extension == "edu":    #Change this to whatever.
            raise forms.ValidationError("Please use a valid .edu email address") #Change message here.
        return email

class ApplicationNew(forms.ModelForm):
    class Meta:
        model = ApplicationNew
        fields = ['full_name', 'email', 'description', 'description2', 'address', 'zipcode', 'state', 'city', 'country']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if not extension == "edu":
            raise forms.ValidationError("Please use a valud .edu email")
        return email
