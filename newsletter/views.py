from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.

def home(request):
    title = "Welcome"
    #if request.user.is_authenticated():
        #title = "MVP %s" %(request.user)
    if request.method == "POST":
        print request.POST
    form = SignUpForm()
    context = {
        "template_title": title,
        "form": form,
}
    return render(request, "home.html", context)
