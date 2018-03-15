from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourites = models.ManyToManyField('Sandwich', blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Sandwich(models.Model):
    creator = models.ForeignKey(Profile, on_delete=models.PROTECT)
    name = models.CharField(max_length=256, unique=True)
    image = models.ImageField(blank=True)
    ingredients = models.ManyToManyField('Ingredient')
    likes = models.PositiveIntegerField(blank=True, default=0)
    dislikes = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sandwiches"

class Ingredient(models.Model):
    name = models.CharField(max_length=128, unique=True)
    calories = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    sandwich = models.ForeignKey(Sandwich, on_delete=models.PROTECT)
    comment = models.TextField()

    def __str__(self):
        return self.comment
