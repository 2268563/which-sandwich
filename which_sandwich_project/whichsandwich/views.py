Skip to content
This repository
Search
Pull requests
Issues
Marketplace
Explore
 @2260469s
Sign out
1
0 0 2268563/which-sandwich
 Code  Issues 4  Pull requests 0  Projects 1  Wiki  Insights
which-sandwich/which_sandwich_project/whichsandwich/views.py
b65dc79  15 minutes ago
 Quentin Deligny Minor updates to views
     
243 lines (185 sloc)  8.31 KB
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
    # Placeholder - returns index for now
    return render(request, 'whichsandwich/index.html')

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
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves,
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and
            #put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
            # Now we save the UserProfile model instance.
            profile.save()
            
            # Update our variable to indicate that the template
            # registration was successful.
            registered = True
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors, profile_form.errors)
    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    # Render the template depending on the context.
    return render(request,
                  'whichsandwich/sign_up.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
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
    
    
    context_dict = {'User' : request.user}
    
    
    response = render(request, 'whichsandwich/my_account.html', context = context_dict)
    return response

@login_required
def my_sandwiches(request):
#    creators = Sandwich.objects.get('creator')
#    users = User.objects.get('user')
    my_sandwiches = Sandwich.objects.filter(username = creator)
#    for user in users:
#        for creator in creators:
#            if user == creators:
#                my_sandwiches = my_sandwiches + 

    # Placeholder - returns index for now
    return render(request, 'whichsandwich/index.html')

@login_required
def my_favourites(request):
    
    context_dict = {}
    
    try:
        # If we can't, the .get() method raises a DoesNotExist exception.
        favourites = User.objects.get('favourites')
        context_dict['My Favourites'] = favourites
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
            sandwich.save
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
© 2018 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
API
Training
Shop
Blog
About
Press h to open a hovercard with more details.