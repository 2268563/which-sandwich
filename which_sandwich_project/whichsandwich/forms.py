from django import forms
from django.contrib.auth.models import User
from whichsandwich.models import Profile, Sandwich, Ingredient, Comment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'favourites')

# May need to add forms for sandwiches (for adding)
