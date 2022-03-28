from django.shortcuts import render
from allusers.serializers import UserProfileSerializer,GetFavouritePetsSerializer,AddFavouritePetsSerializer
from allusers.models import UserProfile,FavouritePets
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class UserProfileModelViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['session']

class GetFavouritePetsModelViewSet(viewsets.ModelViewSet):
    queryset = FavouritePets.objects.all()
    serializer_class = GetFavouritePetsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

class AddFavouritePetsModelViewSet(viewsets.ModelViewSet):
    queryset = FavouritePets.objects.all()
    serializer_class = AddFavouritePetsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']