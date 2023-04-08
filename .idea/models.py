from django.db import models
class Breed(models.Model):
    SIZE CHOICES = (

    )

name = models.CharField(max_length=255)
size = models.CharField(max_length= 255)
friendlyness = models.IntegerField()

