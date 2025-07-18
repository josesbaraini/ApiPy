from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from client.models import Client
from client.serializers import ClientModelSerializer
from App.permisions import GlobalPermissionClass

class ClientCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset=Client.objects.all().prefetch_related('emails')
    serializer_class = ClientModelSerializer

class ClientRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset=Client.objects.prefetch_related('emails').all()
    serializer_class = ClientModelSerializer