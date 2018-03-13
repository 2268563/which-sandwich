from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from whichsandwich.models import User, Sandwich, Ingredient, Comment
from django.core.urlresolvers import reverse


def home(request):
    #http://127.0.0.1:8000/whichsandwich/
    return HttpResponse("Welcome to the home page!")

def browse(request):

def top(request):

def new(request):

def controversial(request):

def sandwich_name(request):


def sign_up(request):
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes value to
    # True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    #if request.method == 'POST':

    #need to set up forms to go further.

def sign_in(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:

             # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your WhichSandwich account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
        
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        return render(request, 'whichsandwich/sign_in.html', {})

@login_required
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def my_account(request):

@login_required
def my_sandwiches(request):

@login_required
def my_favourites(request):
    

@login_required
def create_sandwich(request):
    

def about(request):

# This will be used for all restricted views.
@login_required
def restricted(request):
     return render(request, 'rango/restricted.html', {})
