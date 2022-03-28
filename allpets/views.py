from django.shortcuts import render
from rest_framework import viewsets
from allpets.serializers import PetBreedSerializer
from allpets.models import PetBreed
from rest_framework.permissions import IsAdminUser,BasePermission,SAFE_METHODS
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class PetBreedModelViewSet(viewsets.ModelViewSet):
    queryset = PetBreed.objects.all()
    serializer_class = PetBreedSerializer
    permission_classes = [IsAdminUser|ReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['breed']

