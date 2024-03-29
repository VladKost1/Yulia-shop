from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from accounts.forms import SignUpForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, ("There Was An Error Logging In, Try Again..."))
            return redirect('/accounts/account')
    else:
        return render(request, 'account.html', {})


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, ("Registrations Successful!"))
            return redirect('/accounts/account')
    else:
        form = SignUpForm()

    return render(request, "register_user.html", {'form': form})
