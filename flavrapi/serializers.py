from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer
from .models import Recipe
from rest_framework import serializers
class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username','first_name', 'password', 're_password')

        def validate(self, attrs):
            if 'username' not in attrs or not attrs['username']:
                email =attrs.get('email', '')
                attrs['username'] = email.split('@')[0] or f'user_{User.objects.count() + 1}'
            return super().validate(attrs)
        

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe 
        fields = [
            'id', 'name', 'description', 'created_at'
        ]