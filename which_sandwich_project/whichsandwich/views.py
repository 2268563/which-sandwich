from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from whichsandwich.models import User, Sandwich, Ingredient, Comment
from whichsandwich.forms import UserForm, UserProfileForm, SandwichForm
from django.urls import reverse


def index(request):
    #http://127.0.0.1:8000/whichsandwich/

    top_sandwiches = Sandwich.objects.order_by('-likes')[:5]

    context_dict = {'top_sandwiches': top_sandwiches}

    response = render(request, 'whichsandwich/index.html', context = context_dict)
    return response

    #How do we define sandwich of the day

def browse(request):
    context_dict = {}
    
    try:
        # If we can't, the .get() method raises a DoesNotExist exception.
        sandwiches = Sandwich.objects.all()
        context_dict['sandwiches'] = sandwiches
    except Sandwich.DoesNotExist:
        context_dict['wandwiches'] = None
        
    response = render(request, 'whichsandwich/browse.html', context = context_dict)
    return response

def show_sandwich(request, sandwich_slug):
    context_dict = {}

    try:
        sandwich = Sandwich.objects.get(slug=sandwich_slug)
        context_dict['sandwich'] = sandwich
    except Sandwich.DoesNotExist:
        context_dict['sandwich'] = None

    return render(request, 'whichsandwich/sandwich.html', context_dict)

def top(request):
    top_sandwiches = Sandwich.objects.order_by('-likes')
    
    context_dict = {'Top Sandwiches': top_sandwiches}
    response = render(request, 'whichsandwich/browse.html', context = context_dict)
    return response

def new(request):

    new_sandwiches = Sandwich.objects.order_by('created_date')
    
    context_dict = {'New Sandwiches': new_sandwiches}
    response = render(request, 'whichsandwich/browse.html', context = context_dict)
    return response

def controversial(request):

    likes = Sandwich.objects.get('likes')
    dislikes = Sandwich.objects.get('dislikes')

    #After a set number of likes & dislikes, a sandwich becomes controversial
    #We then order them starting with those with the closest number of likes & dislikes
    if likes>=5 and dislikes>=5:
        controversial_sandwiches = Sandwich.objects.order_by(abs('likes'-'dislikes'))
    
        context_dict = {'Controversial_sandwiches': controversial_sandwiches}

    else:
        context_dict = {'Controversial_sandwiches': None}
    response = render(request, 'whichsandwich/browse.html', context = context_dict)
    return response

def sandwich_name(request):
    
    context_dict = {}
    try:
        # If we can't, the .get() method raises a DoesNotExist exception.
        names = Sandwich.objects.get('name')
        context_dict['Sandwich Names'] = names
    except Category.DoesNotExist:
        context_dict['Sandwich Names'] = None
        
    response = render(request, 'whichsandwich/browse.html', context = context_dict)
    return response


def sign_up(request):
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes value to
    # True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        user_form = UserForm(data=request.POST)
        
        # If the two forms are valid...
        if user_form.is_valid():
            # Create the user instance
            user = user_form.save(commit=False)
            
            # Now we hash the password with the set_password method.
            user.set_password(user.password)
            
            # User profile is created automatically
            
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and
            # put it in the UserProfile model.
            if 'picture' in request.FILES:
                user.profile.picture = request.FILES['picture']
                
            # Now we save the UserProfile model instance.
            user.save()
            
            # Update our variable to indicate that the template
            # registration was successful.
            registered = True
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors)
    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        
    # Render the template depending on the context.
    return render(request,
                  'whichsandwich/sign_up.html',
                  {'user_form': user_form,
                   'registered': registered})

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
    best_sandwiches = Sandwich.objects.filter(creator=request.user).order_by('-likes', 'dislikes')

    context_dict = {
            'best_sandwiches': best_sandwiches,
            }

    return render(request, 'whichsandwich/my_account.html', context = context_dict)

@login_required
def my_sandwiches(request):

    my_sandwiches = Sandwich.objects.filter(creator=request.user)

    context_dict = {'my_sandwiches':my_sandwiches}

    return render(request, 'whichsandwich/my_sandwiches.html',context = context_dict)

@login_required
def my_favourites(request):
    
    context_dict = {}
    
    try:
        # If we can't, the .get() method raises a DoesNotExist exception.
        my_favourites = User.objects.filter(user = request.user)
        context_dict['My Favourites'] = my_favourites
    except User.DoesNotExist:
        context_dict['My Favourites'] = None
        
    response = render(request, 'whichsandwich/my_favourites.html', context = context_dict)
    return response

@login_required
def create_sandwich(request):
    creator = request.user
    form = SandwichForm()

    if request.method == 'POST':
        form = SandwichForm(request.POST)

        if form.is_valid():
            sandwich = form.save(commit=False)
            sandwich.creator = creator
            sandwich.save()
            form.save_m2m()
            return show_sandwich(request, sandwich.slug)
        else:
            print(form.errors)

    return render(request, 'whichsandwich/create_sandwich.html', {'form':form})

def about(request):

    #No need for context_dict if we do not show user's number of visits.
    return render(request, 'whichsandwich/about.html')

# This will be used for all restricted views.
@login_required
def restricted(request):
     return render(request, 'rango/restricted.html', {})
