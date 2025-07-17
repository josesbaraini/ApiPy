from rest_framework import serializers
from client.models import Client
from emails.serializers import EmailSerializer
from phone.serializers import PhoneSerializer

class ClientModelSerializer(serializers.ModelSerializer):
    emails = EmailSerializer(many=True, read_only=True)
    phones = PhoneSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields= "__all__"