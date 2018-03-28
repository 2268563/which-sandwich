import os, sys
import math, random
import shutil
from PIL import Image
from os import listdir

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
        'which_sandwich_project.settings')

import django
django.setup()
from whichsandwich.models import User, Sandwich, Ingredient, Comment
from django.core.files import File
from django.utils.text import slugify

def populate():
    # Constructs random sandwiches from given ingredients and randomly assigns
    # users as the creator from a list of given users.
    # Comments are also randomly assigned to sandwiches from users based on
    # given comment strings.
    # Returns True if population is completed successfully or False if otherwise

    # Make sure we're in the script's directory
    os.chdir(sys.path[0])

    # Delete the user_images folder if there are no users
    try:
        if not User.objects.all():
            print(" - Deleting expired user data")
            shutil.rmtree('media/user_images', ignore_errors=True)
    except django.db.utils.OperationalError as e:
        print("Error: %s\nDid you remember to migrate?" % e)
        return False;

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

    sandwich_stock_images = []
    ## Get stock images
    os.chdir(os.pardir)
    os.chdir('stock_sandwich_images')

    for image in os.listdir():
        sandwich_image_path = os.path.join(os.getcwd(), image)
        sandwich_stock_images.append(File(open(sandwich_image_path, 'rb')))

    # Generate sandwiches
    print(" - Generating random sandwiches")
    for image in sandwich_stock_images:
        sandwiches.append(random_sandwich(user_objects, ingredient_objects, image))

    sandwich_objects = []

    # Add sandwiches to database
    print(" - Adding sandwiches to database")
    for sandwich in sandwiches:
        sandwich_objects.append(add_sandwich(sandwich))

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
        u.profile.favourites.add(*rand_selection(sandwich_objects, 0))
        u.save()

    # Population completed successfully
    return True

def add_user(username, email):
    u = User.objects.get_or_create(username=username, email=email)[0]
    u.save()
    return u

def add_ingredient(name, calories):
    i = Ingredient.objects.get_or_create(name=name, calories=calories)[0]
    i.save()
    return i

def add_sandwich(sandwich):
    creator = sandwich['creator']
    name = sandwich['name']
    ingredients = sandwich['ingredients']
    image = sandwich['image']

    # Need this to check for existing sandwiches.
    # It is not passed here on object creation since it is automatically 
    # generated in models
    temp_slug = slugify(name)

    # Check if sandwich already exists in database
    s = Sandwich.objects.filter(slug=temp_slug)
    if s.exists():
        return s[0]

    s = Sandwich.objects.create(creator=creator, name=name, image=image)

    # Add ingredients for new sandwich
    for ingr in ingredients:
        s.ingredients.add(ingr)
    s.likes = random.randint(0,100)
    s.dislikes = random.randint(0,50)

    s.save()
    image.close()
    return s

def add_comment(user, sandwich, comment):
    c = Comment.objects.get_or_create(user=user, sandwich=sandwich, comment=comment)[0]
    c.save()
    return c

def random_sandwich(users, ingredients, image):
    creator = users[random.randint(0, len(users)-1)]
    used_ingr = rand_selection(ingredients, 1)

    name = used_ingr[0].name

    if len(used_ingr) > 1:
        name += " and " + used_ingr[1].name

    return {
            'creator':creator, 
            'name':name, 
            'ingredients':used_ingr,
            'image':image
            }

def random_comment(users, sandwiches, comments):
    user = rand_selector(users).profile
    sandwich = rand_selector(sandwiches) 
    comment = rand_selector(comments)
    return {'user':user, 'sandwich':sandwich, 'comment':comment}               

def rand_selector(l):
    # Returns a random element from the given list
    return l[random.randint(0,len(l)-1)]

def rand_selection(items, minimum):
    # Returns a random selection from the given list.
    # The minimum number of selections can be passed in.
    
    if minimum < 0:
        minimum = 0

    items = items[:]
    total = random.randint(minimum, math.ceil(len(items)/2))
    selected_items = []
    for i in range(total):
        selected_items.append(items.pop(random.randint(0, len(items)-1)))
    return selected_items

if __name__ == '__main__':
    print("Starting Which Sandwich population script...")
    if populate():
        print("Population completed")
    else:
        print("Population failed\nCheck errors and try again")
