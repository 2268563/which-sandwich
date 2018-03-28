from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from whichsandwich.models import Profile, Sandwich, Ingredient, Comment
from whichsandwich.forms import UserForm, UserProfileForm, SandwichForm, CommentForm
from django.urls import reverse
import random

def index(request):
    #http://127.0.0.1:8000/whichsandwich/

    sotd = None
    top_sandwiches = Sandwich.objects.order_by('-likes')
    if top_sandwiches:
        sotd = top_sandwiches[0]

    context_dict = {
            'top_sandwiches': top_sandwiches[1:5],
            'sotd': sotd,
            }

    response = render(request, 'whichsandwich/index.html', context = context_dict)
    return response

    #How do we define sandwich of the day

def browse(request):
    return render(request, 'whichsandwich/browse.html')

def modal(request):
    context_dict = {}
    if request.method == 'GET':
        sandwich_id = request.GET['sandwich_id']
        sandwich = Sandwich.objects.get(id=sandwich_id)
        context_dict['sandwich'] = sandwich
        try:
            comments = Comment.objects.filter(sandwich=sandwich)
            rand_comment_index = random.randint(0,len(comments) - 1)
            context_dict['comment'] = comments[rand_comment_index]
        except (IndexError, ValueError) as e:
            print(e)
            context_dict['comment'] = None
    return render(request, 'whichsandwich/modal.html', context_dict)

def browse_filter(request):
    sort_filter = None
    if request.method == 'GET':
        sort_filter = request.GET['sort_filter']
    if sort_filter == 'new':
        return new(request)
    elif sort_filter == 'controversial':
        return controversial(request)
    else:
        # Top by default
        return top(request)

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
    response = render(request, 'whichsandwich/sandwich_grid.html', context = context_dict)
    return response

def new(request):
    new_sandwiches = Sandwich.objects.order_by('-created_date')
    
    context_dict = {'sandwiches': new_sandwiches}
    response = render(request, 'whichsandwich/sandwich_grid.html', context = context_dict)
    return response

def controversial(request):
    # Maximum percentage difference between likes and dislikes for controversy
    max_perc_diff = 25

    # After a set number of likes & dislikes, a sandwich becomes elligible for controversy
    sandwiches = Sandwich.objects.filter(likes__gt=10, dislikes__gt=10)

    c_sandwiches = []

    # Get controversial sandwiches
    for sandwich in sandwiches:
        delta = abs(sandwich.likes - sandwich.dislikes)
        avg = (sandwich.likes + sandwich.dislikes)/2
        c_level = delta/avg*100
        if c_level <= max_perc_diff:
            # Add controversial sandwich to list alongside percentage difference
            # between likes and dislikes
            c_sandwiches.append([c_level, sandwich])

    # Sort sandwiches by difference between likes and dislikes
    c_sandwiches = sorted(c_sandwiches, key=lambda s: s[0])
    # Retrieve just the sandwich
    c_sandwiches = [s for c,s in c_sandwiches]
    
    return render(request, 'whichsandwich/sandwich_grid.html', {'sandwiches': c_sandwiches})

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
    sandwiches = Sandwich.objects.filter(creator=request.user)
    context_dict = {'sandwiches': sandwiches}
    return render(request, 'whichsandwich/my_sandwiches.html',
            context = context_dict)

@login_required
def my_favourites(request):
    context_dict = {}
    favourites = request.user.profile.favourites.all()
    context_dict['sandwiches'] = favourites
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
    creator = request.user.profile
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
