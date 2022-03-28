from django.contrib import admin
from allusers.models import UserProfile,FavouritePets
# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=('id','user','session')
    

@admin.register(FavouritePets)
class FavouritePetsAdmin(admin.ModelAdmin):
    list_display=('id','user','pet')
    
