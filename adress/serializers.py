from rest_framework import serializers
from adress.models import Adress


class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = '__all__'
