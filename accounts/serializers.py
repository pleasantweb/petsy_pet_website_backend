from rest_framework import serializers
from djoser.serializers import UserCreateSerializer,UserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

###########################################################################

class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields =('id','email','first_name','last_name','is_staff')
   
#############################################################################

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email','first_name','last_name','password')