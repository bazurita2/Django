from rest_framework import serializers
from .models import Usercrud


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usercrud
        fields = '__all__'
