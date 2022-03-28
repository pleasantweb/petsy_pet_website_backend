from django.db import models
from accounts.models import UserAccounts
from allpets.models import PetBreed
# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(UserAccounts, on_delete=models.CASCADE,blank=True,null=True)
    session = models.CharField(max_length=100,unique=True,blank=True,null=True)

class FavouritePets(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pet= models.ForeignKey(PetBreed, on_delete=models.CASCADE)