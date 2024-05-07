from django.db import models

# Create your models here.

class Employe(models.Model):
    name = models.CharField(max_length=50)
    si = models.IntegerField()
    age = models.IntegerField()
    income = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    image = models.FileField()

    def __str__(self):
        return self.name