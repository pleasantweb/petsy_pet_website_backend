from django.contrib import admin
from allpets.models import PetBreed
# Register your models here.
@admin.register(PetBreed)
class PetBreedAdmin(admin.ModelAdmin):
    list_display = ('id','breed')
    

