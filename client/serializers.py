from rest_framework import serializers
from client.models import Client
from adress.serializers import AdressSerializer

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields= "__all__"