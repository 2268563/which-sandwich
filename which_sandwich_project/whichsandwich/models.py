from django.db import models

class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.username

class Sandwich(models.Model):
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=254, unique=True)
    image = models.ImageField()
    ingredients = models.ManyToManyField('Ingredient')
    comments = models.ManyToManyField('Comment')

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
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.comment
