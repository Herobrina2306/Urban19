from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balanse = models.DecimalField(decimal_places=2, max_digits=7)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=70)
    cost = models.DecimalField(decimal_places=2, max_digits=7)
    size = models.DecimalField(decimal_places=3, max_digits=8)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=75)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
