import logging

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.management import call_command
from django.db import IntegrityError
from django.shortcuts import render, redirect
from faker import Faker
from search.documents import HelpdeskDocument
# Create your views here.
from search.models import HelpdeskModel


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
                logging.warning(f" logging in {request.POST['username']}")
                return redirect('search')
            except IntegrityError:
                # If username already exists show error
                logging.warning(f"{request.POST['username']} is taken. Please try again")
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
            logging.warning("Username or password didn't match")
            return render(request, 'search/loginuser.html',
                          {'form': AuthenticationForm(),
                           'error': "Username or password didn't match"})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginuser')


@login_required
def search(request):
    return render(request, 'search/search.html')


@login_required
def searchresults(request):
    query = request.GET.get('query')
    if query:
        query = str(query).strip()
    logging.info(query)
    s = HelpdeskDocument.search().query("match", title=query).query("match", details=query)
    qs = s.to_queryset()

    return render(request, 'search/searchresults.html', {'query': query, 'results': qs})


def generate_fake_data():
    logging.info("generating fake data!")
    fake = Faker()
    keywords = ['help', 'ticket', 'support', 'data', 'tech', 'computer', 'hardware', 'software', 'dashboard', 'rating',
                'install', 'working', 'admin', 'IT', 'supervisor', 'manager', 'error', 'missing', 'not installed',
                'not starting', 'failure', 'boot']
    for _ in range(10):
        title = fake.sentence(ext_word_list=keywords)
        details = fake.sentence(ext_word_list=keywords) + fake.sentence()
        owner = fake.name()
        hd = HelpdeskModel(title=title.rstrip('.'), details=details, owner=owner)
        hd.save()
    logging.info('rebuilding elasticsearch index after data creation')
    call_command('search_index', '--rebuild', '-f')


def home(request):
    if request.user.is_authenticated:
        return redirect('search')
    else:
        generate_fake_data()
        return render(request, 'search/home.html')
