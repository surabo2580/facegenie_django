from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, 'home.html')


def handleSignup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) > 10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')
        if username.isalpha():
            messages.error(request, "username can't only contains alphabet")
            return redirect('home')
        if username.isnumeric():
            messages.error(request, "username can't only contain numeric value")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if User.objects.filter(username=username).exists():
            messages.error(request, "username already exists")
            return redirect('home')
        if User.objects.filter(email=email).exists():
            messages.error(request, "email already exists")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, " Passwords do not match")
            return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, " Your accounts has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #captcha = request.POST.get('cap')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'successfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('home')
    #messages.error(request, 'invalidcaptcha')
    return redirect('home')


def handlelogout(request):
    logout(request)
    messages.success(request,'you have successfully logged out')
    return redirect('home')