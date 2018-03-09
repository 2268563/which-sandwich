from django.contrib import admin
from whichsandwich.models import User,Sandwich,Comment,Ingredient

# Register your models here.

admin.site.register(User)
admin.site.register(Sandwich)
admin.site.register(Comment)
admin.site.register(Ingredient)
