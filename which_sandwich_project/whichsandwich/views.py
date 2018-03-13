from django.shortcuts import render
from django.http import HttpResponse




def home(request):
    #http://127.0.0.1:8000/whichsandwich/
    return HttpResponse("Welcome to the home page!")

'''
def browse(request):

def top(request):

def new(request):

def controversial(request):

def sandwich_name(request):


def sign_up(request):
    

def sign_in(request):
    

def my_account(request):

def my_sandwiches(request):

def my_favourites(request):
    

def create_sandwich(request):
    

def about(request):

'''

