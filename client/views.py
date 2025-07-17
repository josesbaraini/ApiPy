from rest_framework import generics
from client.models import Client
from client.serializers import ClientModelSerializer

class ClientCreateListView(generics.ListCreateAPIView):
    queryset=Client.objects.all().prefetch_related('emails')
    serializer_class = ClientModelSerializer

class ClientRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Client.objects.prefetch_related('emails').all()
    serializer_class = ClientModelSerializer