# django_project/users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from Users.forms import UserRegistrationForm

# Create your views here.
def register(request):
    # Logged in user can't register a new account
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = UserRegistrationForm()

    return render( request = request, template_name = "registration/register.html", context={"form":form})
