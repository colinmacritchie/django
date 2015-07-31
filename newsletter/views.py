from django.shortcuts import render
from .forms import SignUpForm, ContactForm
# Create your views here.

#Function that displays and saves the form.
def home(request):
    title = "Welcome"
    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form,
}


#Displays Thank you message after form is submitted.
    if form.is_valid():
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name

        instance.save()
        context = {
            "title": "Thank You!"

        }

#renders the request, view, and context.
    return render(request, "home.html", context)
#End of Home View.

#Start of Contact View
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        full_name = form.cleaned_data.get("full_name")
        message = form.cleaned_data.get("message")
        print email, message, full_name

    context = {
        "form": form,
    }

    return render(request, "forms.html", context)
