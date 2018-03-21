from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from whichsandwich.models import Profile,Sandwich,Comment,Ingredient

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

class SandwichAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', )

# Register your models here.

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Sandwich, SandwichAdmin)
admin.site.register(Comment)
admin.site.register(Ingredient)
