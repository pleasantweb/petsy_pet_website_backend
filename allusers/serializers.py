from rest_framework import serializers
from allusers.models import UserProfile,FavouritePets
from allpets.serializers import PetBreedSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','user','session')

class GetFavouritePetsSerializer(serializers.ModelSerializer):
    pet = PetBreedSerializer(read_only=True)
    class Meta:
        model = FavouritePets
        fields = ('id','user','pet')

class AddFavouritePetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouritePets
        fields = ('id','user','pet')