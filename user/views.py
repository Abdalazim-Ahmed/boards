from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login as auth_login


# Create your views here.


def signup(request):

    form = SignupForm()
    if request.method == "POST":
       form = SignupForm(request.POST)
       if form.is_valid():
           user = form.save()
           auth_login(request, user)

           return redirect('home')
    else:
       form = SignupForm()       

    return render(request, 'user/signup.html', {'form':form})