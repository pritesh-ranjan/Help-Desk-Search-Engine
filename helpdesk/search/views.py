from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect


# Create your views here.
def signupuser(request):
    if request.method == 'GET':
        # Load the signup page if it is a GET request
        return render(request, 'search/signupuser.html', {'form': UserCreationForm()})
    elif request.method == 'POST':
        # Create a new user if it is a POST request
        if request.POST['password1'] == request.POST['password2']:
            try:
                print(request.POST['username'], request.POST['password1'])
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)  # finally login
                return redirect('search')
            except IntegrityError:
                # If username already exists show error
                return render(request, 'search/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': f"{request.POST['username']} is taken. Please try again"})
        else:
            # Tell user passwords didn't match!
            return render(request, 'search/signupuser.html', {'form': UserCreationForm(),
                                                              'error': "Passwords didn't match"})


def loginuser(request):
    if request.method == 'GET':
        # Load the login page if it is a GET request
        return render(request, 'search/loginuser.html', {'form': AuthenticationForm()})
    elif request.method == 'POST':
        # If it is a POST request, check if the user exists and credentials are correct
        #  and the login the user
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)  # finally login
            return redirect('search')
        else:
            return render(request, 'search/loginuser.html',
                          {'form': AuthenticationForm(),
                           'error': "Username or password didn't match"})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def search(request):
    return render(request, 'search/search.html')


@login_required
def searchresults(request):
    query = request.GET.get('query')
    if query:
        query = str(query).strip()

    return render(request, 'search/searchresults.html', {'query': query})


def home(request):
    return render(request, 'search/home.html')
