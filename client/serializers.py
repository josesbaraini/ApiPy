from rest_framework import serializers
from client.models import Client
from emails.serializers import EmailSerializer
from phone.serializers import PhoneSerializer

class ClientSerializer(serializers.ModelSerializer):
    emails = EmailSerializer(many=True)
    class Meta:
        model = Client
        fields= "__all__"