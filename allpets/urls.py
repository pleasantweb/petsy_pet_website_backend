from django.urls import path,include
from rest_framework.routers import DefaultRouter
from allpets.views import PetBreedModelViewSet

router = DefaultRouter()

router.register('petbreed',PetBreedModelViewSet,basename='petbreed' )

urlpatterns = [
    path('pet/',include(router.urls))
]
