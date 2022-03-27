from rest_framework import serializers
from allpets.models import PetBreed

class PetBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetBreed
        fields = ('id','breed','bred_for','life_span','temprament','origin','price','image','description')
