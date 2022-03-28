from django.urls import path,include
from rest_framework.routers import DefaultRouter
from allusers.views import UserProfileModelViewSet,GetFavouritePetsModelViewSet,AddFavouritePetsModelViewSet
router = DefaultRouter()

router.register('user_profile', UserProfileModelViewSet,basename='user_profile')
router.register('favourite',GetFavouritePetsModelViewSet,basename='favourite' )
router.register('add_favourite', AddFavouritePetsModelViewSet,basename='add_favourite')

urlpatterns = [
    path('alluser/',include(router.urls))
]
