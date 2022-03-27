from django.db import models

# Create your models here.
class PetBreed(models.Model):
    breed = models.CharField(max_length=100)
    bred_for=models.CharField(max_length=100)
    life_span=models.CharField(max_length=100)
    temprament=models.CharField(max_length=100)
    origin=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    image=models.CharField(max_length=100)
    description = models.TextField()

