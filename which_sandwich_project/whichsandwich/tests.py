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
        
        sd = Sandwich(creator = User(), slug='Random Sandwich String')
        sd.save()
        self.assertEqual(Sandwich.slug, 'random-category-string')
    '''
    def test_ensure_sandwich_has_name(self):
        sd = Sandwich(name= '')
        sd.__str__()
        self.assertEqual((sd.name != ''), True)
'''
    def test_ensure_likes_are_positive(self):
        user = User()
        sd_likes = Sandwich( likes=-1)
        sd_likes.save()
        self.assertEqual((sd_likes >= 0), True)

    def test_ensure_dislikes_are_positive(self):
        user = Profile()
        sd_dislikes = Sandwich( dislikes=-1)
        sd_dislikes.save()
        self.assertEqual((sd_dislikes >= 0), True)
'''
    

class IngredientMethodTests(TestCase):
    def test_ensure_ingredient_has_name(self):
        ing = Ingredient(name= '')
        ing.__str__()
        self.assertEqual((ing.name != ''), True)

class CommentMethodTests(TestCase):
    def test_ensure_comment_not_empty(self):
        com = Comment(comment = '')
        com.__str__()
        self.assertEqual((com.comment != ''), True)
