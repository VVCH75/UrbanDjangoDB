from django.db import models

class Bayer(models.Model):
    name = models.CharField(max_length=25)
    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    age = models.IntegerField(max_length=2, default=0)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField(decimal_places=2, max_digits=10, default=100)
    size = models.DecimalField(decimal_places=4, max_digits=10, default=10)
    description = models.TextField(max_length=500, default=500)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Bayer, related_name='games')

    def __str__(self):
        return self.title