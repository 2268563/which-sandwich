from django.db import models

class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    favourites = models.ManyToManyField('Sandwich', blank=True)

    def __str__(self):
        return self.username

class Sandwich(models.Model):
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
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
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    sandwich = models.ForeignKey(Sandwich, on_delete=models.PROTECT)
    comment = models.TextField()

    def __str__(self):
        return self.comment
