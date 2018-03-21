from django import forms
from django.contrib.auth.models import User
from whichsandwich.models import User, Sandwich, Ingredient, Comment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user', 'favourites')

class SandwichForm(forms.ModelForm):
    class Meta:
        model = Sandwich
        fields = ('name', 'image', 'ingredients')
