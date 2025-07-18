from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from client.models import Client
from client.serializers import ClientModelSerializer

class ClientCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Client.objects.all().prefetch_related('emails')
    serializer_class = ClientModelSerializer

class ClientRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Client.objects.prefetch_related('emails').all()
    serializer_class = ClientModelSerializer