from rest_framework import serializers
from .models import Solve
from django.contrib.auth.models import User

class SolveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solve
        fields = '__all__'
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
