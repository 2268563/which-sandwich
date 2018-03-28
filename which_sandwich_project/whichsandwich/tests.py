from django.test import TestCase
from whichsandwich.models import Profile, Sandwich, Ingredient, Comment
from django.contrib.auth.models import User

'''
class ProfileMethodTests(TestCase):
    def test_ensure_user_not_blank(self):
        #Should be True if user attribute of Profile is not blank
        user_test = Profile(user = None)
        user_test.__str__()
        self.assertEqual((user_test.user != ''), True)
'''
class SandwichMethodTests(TestCase):
    '''
    def test_slug_line_creation(self):
        #slug_line_creation checks to make sure that when we add a category an appropriate slug line is created
        #i.e. "Random Category String" -> "random-category-string"
        user = User.objects.create_user(username = 'max',
                                        email = 'max@test.com',
                                        password = 'mario')
        sd = Sandwich(creator = user, slug ='Random Sandwich String')
        sd.save()
        self.assertEqual(sd.slug, 'random-sandwich-string')
    
    def test_ensure_sandwich_has_ingredients(self):
        ing = Ingredient(name='',calories=0)
        sd_ing = Sandwich(ingredients = ing)
        sd_ing.save()
        self.assertEqual((sd_ing.ingredients != ing),True)
    '''
    def test_ensure_sandwich_has_name(self):
        sd = Sandwich(name= '')
        sd.__str__()
        self.assertEqual((sd.name != ''), True)

    def test_ensure_likes_are_positive(self):
        user = User.objects.create_user(username = 'max',
                                        email = 'max@test.com',
                                        password = 'mario')
        sd_likes = Sandwich(creator = user, likes=-1)
        sd_likes.save()
        self.assertEqual((sd_likes.likes >= 0), True)

    def test_ensure_dislikes_are_positive(self):
        user = User.objects.create_user(username = 'max',
                                        email = 'max@test.com',
                                        password = 'mario')
        sd_dislikes = Sandwich(creator = user, dislikes=-1)
        sd_dislikes.save()
        self.assertEqual((sd_dislikes.dislikes >= 0), True)

    

class IngredientMethodTests(TestCase):
    def test_ensure_ingredient_has_name(self):
        ing = Ingredient(name= '')
        ing.__str__()
        self.assertEqual((ing.name != ''), True)

    def test_ensure_calories_are_positive(self):
        cal = Ingredient(name = 'test', calories = -1)
        cal.save()
        self.assertEqual((cal.calories >= 0), True)

class CommentMethodTests(TestCase):
    def test_ensure_comment_not_empty(self):
        com = Comment(comment = '')
        com.__str__()
        self.assertEqual((com.comment != ''), True)
