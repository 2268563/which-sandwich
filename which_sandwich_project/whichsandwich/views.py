from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from whichsandwich.models import Profile, Sandwich, Ingredient, Comment
from whichsandwich.forms import UserForm, UserProfileForm, SandwichForm, CommentForm
from django.urls import reverse


def index(request):
    #http://127.0.0.1:8000/whichsandwich/

    top_sandwiches = Sandwich.objects.order_by('-likes')
    sotd = top_sandwiches[0]

    context_dict = {
            'top_sandwiches': top_sandwiches[1:5],
            'sotd': sotd,
            }

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
    creator = request.user
	
    try:
        creator = Profile.objects.get(user=creator)
        context_dict['favourites'] = creator.favourites.all();
    except:
        context_dict['favourites'] = None
	
    try:
        sandwich = Sandwich.objects.get(slug=sandwich_slug)
        context_dict['sandwich'] = sandwich
        comments = Comment.objects.filter(sandwich=sandwich)
        context_dict['comments'] = comments
    except Sandwich.DoesNotExist:
        context_dict['sandwich'] = None
        context_dict['comments'] = None
    return render(request, 'whichsandwich/sandwich.html', context_dict)

def top(request):
    top_sandwiches = Sandwich.objects.order_by('-likes')
    
    context_dict = {'sandwiches': top_sandwiches}
    response = render(request, 'whichsandwich/browse.html', context = context_dict)
    return response

def new(request):

    new_sandwiches = Sandwich.objects.order_by('-created_date')
    
    context_dict = {'sandwiches': new_sandwiches}
    response = render(request, 'whichsandwich/browse.html', context = context_dict)
    return response

def controversial(request):
    context_dict = {}
    controversial_sandwiches = []
    sandwiches = Sandwich.objects.all() 

    #After a set number of likes & dislikes, a sandwich becomes controversial
    #We then order them starting with those with the closest number of likes & dislikes
    for i in sandwiches:
        if i.likes>=5 and i.dislikes>=5:
            controversial_sandwiches.append(i)

    context_dict['sandwiches'] = controversial_sandwiches
    
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

@login_required
def my_account(request):
    best_sandwiches = Sandwich.objects.filter(creator=request.user).order_by('-likes', 'dislikes')
    top_favourites = request.user.profile.favourites.all().order_by('-likes', 'dislikes')[0:5]

    context_dict = {
            'best_sandwiches': best_sandwiches,
			'top_favourites': top_favourites,
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
    favourites = request.user.profile.favourites.all()
    print(favourites)
    context_dict['favourites'] = favourites
    return render(request, 'whichsandwich/my_favourites.html', context=context_dict)

@login_required
def create_sandwich(request):
    form = SandwichForm()

    if request.method == 'POST':
        form = SandwichForm(request.POST, request.FILES)

        if form.is_valid():
            sandwich = form.save(commit=False)
            sandwich.creator = request.user
            sandwich.save()
            form.save_m2m()
            return show_sandwich(request, sandwich.slug)
        else:
            print(form.errors)

    return render(request, 'whichsandwich/create_sandwich.html', {'form':form})

def about(request):

    #No need for context_dict if we do not show user's number of visits.
    return render(request, 'whichsandwich/about.html')

@login_required
def comment(request, sandwich_slug):
    creator = request.user
    creator = Profile.objects.get(user=creator)
    sandwich = Sandwich.objects.get(slug=sandwich_slug)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = creator
            comment.sandwich = sandwich
            comment.save()
            form.save_m2m()
            return show_sandwich(request, sandwich.slug)
        else:
            print(form.errors)

    return render(request, 'whichsandwich/comment.html', {'form':form, 'sandwich':sandwich})

def add_to_favourites(request):
    creator = request.user
    creator = Profile.objects.get(user=creator)
    sw_name = None
    if request.method == 'GET':
        sw_name = request.GET['sandwich_name']
    if sw_name:
        sandwich = Sandwich.objects.get(name=sw_name)
        if sandwich:
            creator.favourites.add(sandwich)
            creator.save()
			
    return HttpResponse("Added to favourites")
	
def like_sandwich(request):
    sw_name = None
    if request.method == 'GET':
        sw_name = request.GET['sandwich_name']
        likes = 0;
    if sw_name:
        sandwich = Sandwich.objects.get(name=sw_name)
        if sandwich:
            likes = sandwich.likes + 1
            sandwich.likes = likes
            sandwich.save()
    return HttpResponse(likes)
	
def dislike_sandwich(request):
    sw_name = None
    if request.method == 'GET':
        sw_name = request.GET['sandwich_name']
        dislikes = 0;
    if sw_name:
        sandwich = Sandwich.objects.get(name=sw_name)
        if sandwich:
            dislikes = sandwich.dislikes + 1
            sandwich.dislikes = dislikes
            sandwich.save()
    return HttpResponse(dislikes)