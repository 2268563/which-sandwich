from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
import os.path

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

def user_directory_path(instance, filename):
    path = 'user_images/user_{0}/'.format(instance.creator.id)
    name = instance.slug + instance.extension()
    return os.path.join(path, name)

class Sandwich(models.Model):
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=256, unique=True)
    image = models.ImageField(upload_to=user_directory_path, blank=True)
    ingredients = models.ManyToManyField('Ingredient')
    likes = models.PositiveIntegerField(blank=True, default=0)
    dislikes = models.PositiveIntegerField(blank=True, default=0)
    slug = models.SlugField(unique=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sandwiches"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def extension(self):
        return os.path.splitext(self.image.name)[1]

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
