import os
import math
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
        'which_sandwich_project.settings')

import django
django.setup()
from whichsandwich.models import User, Sandwich, Ingredient, Comment

def populate():

    users = [
            {'username':"captainsandwich",
                'email':"captsandwich@email.com"},
            {'username':"gowich",
                'email':"gowich@email.com"},
            {'username':"ieatbread",
                'email':"breadeater@email.com"},
            {'username':"cooltoastie",
                'email':"cooltoasties@email.com"},
            ]

    ingredients = [
            {'name':"Ham",
                'calories':141},
            {'name':"Cheese",
                'calories':173},
            {'name':"Chicken",
                'calories':196},
            {'name':"Lettuce",
                'calories':14},
            {'name':"Tomato",
                'calories':6},
            {'name':"Fish Fingers",
                'calories':180},
            {'name':"Peanut Butter",
                'calories':280},
            ]

    comment_strings = [
            "I love this sandwich!",
            "It's okay...",
            "My new favourite :)",
            "Wow!",
            "how do you make a comment?",
            "This site is great!",
            ";)",
            "Too many sandwiches how to choose",
            ]

    user_objects = []
    ingredient_objects = []

    # Add users to database
    print(" - Adding users to database")
    for user in users:
        user_objects.append(add_user(user['username'], user['email']))

    print(" - Adding ingredients to database")
    # Add ingredients to database
    for ingr in ingredients:
        ingredient_objects.append(add_ingredient(ingr['name'], ingr['calories']))

    sandwiches = []
    comments = []

    # Generate sandwiches
    print(" - Generating random sandwiches")
    for i in range(random.randint(10,20)):
        sandwiches.append(random_sandwich(user_objects, ingredient_objects))

    sandwich_objects = []

    # Add sandwiches to database
    print(" - Adding sandwiches to database")
    for sandwich in sandwiches:
        sandwich_objects.append(add_sandwich(sandwich['creator'], sandwich['name'], sandwich['ingredients']))

    # Generate zero or more comments for each sandwich
    print(" - Matching random comments to each sandwich")
    for sandwich in sandwiches:
        for i in range(random.randint(0, len(comment_strings)-1)):
            comments.append(random_comment(user_objects, sandwich_objects, comment_strings))

    # Add comments to database
    print(" - Adding comments to database")
    for comment in comments:
        add_comment(comment['user'], comment['sandwich'], comment['comment'])

    # Populate user favourites lists
    print(" - Populating user favourites")
    for u in user_objects:
        u.favourites.add(*random_favourites(sandwich_objects))
        u.save()

def add_user(username, email):
    u = User.objects.get_or_create(username=username, email=email)[0]
    u.save()
    return u

def add_ingredient(name, calories):
    i = Ingredient.objects.get_or_create(name=name, calories=calories)[0]
    i.save()
    return i

def add_sandwich(creator, name, ingredients):
    s = Sandwich.objects.filter(name=name)
    if s.exists():
        return s[0]
    s = Sandwich.objects.create(creator=creator, name=name)
    for ingr in ingredients:
        s.ingredients.add(ingr)
    s.likes = random.randint(0,10)
    s.dislikes = random.randint(0,10)
    s.save()
    return s

def add_comment(user, sandwich, comment):
    c = Comment.objects.get_or_create(user=user, sandwich=sandwich, comment=comment)[0]
    c.save()
    return c

def random_sandwich(users, ingredients):
    creator = users[random.randint(0, len(users)-1)]
    used_ingr = []

    ingredients = ingredients[:]
    ingr_total = random.randint(1, math.ceil(len(ingredients)/2))

    for i in range(ingr_total):
        used_ingr.append(ingredients.pop(random.randint(0,len(ingredients)-1)))

    # Sort ingredients to avoid duplicates. e.g. Cheese and Ham / Ham and Cheese
    used_ingr.sort(key=lambda k:k.name)

    name = used_ingr[0].name

    if len(used_ingr) > 1:
        name += " and " + used_ingr[1].name

    return {'creator':creator, 'name':name, 'ingredients':used_ingr}

def random_comment(users, sandwiches, comments):
    user = rand_selector(users)
    sandwich = rand_selector(sandwiches) 
    comment = rand_selector(comments)
    return {'user':user, 'sandwich':sandwich, 'comment':comment}               

def rand_selector(l):
    return l[random.randint(0,len(l)-1)]

def random_favourites(sandwiches):
    favourites = []
    for i in range(random.randint(0, len(sandwiches)-1)):
        favourites.append(sandwiches[i])
    return favourites

if __name__ == '__main__':
    print("Starting Which Sandwich population script...")
    populate()
    print("Population completed")
