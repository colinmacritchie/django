from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

def clean_email(self):
    email = self.cleaned_data.get('email')
    email_base, provider = email.split('@')
    domain, extension = provider.split('.')
    #if not extension == "gmail":    #Change this to whatever.
        #raise forms.ValidationError("Please use a valid gmail email address") #Change message here.
    return email


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    #Delete this validation if you want to accept all email types.
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        #if not extension == "gmail":    #Change this to whatever.
            #raise forms.ValidationError("Please use a valid gmail email address") #Change message here.
        return email
