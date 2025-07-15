from rest_framework import generics
from adress.serializers import AdressSerializer
from adress.models import Adress

class AdressCreateListView(generics.ListCreateAPIView):
    queryset=Adress.objects.all()
    serializer_class= AdressSerializer

class AdressRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
        queryset=Adress.objects.all()
        serializer_class= AdressSerializer
