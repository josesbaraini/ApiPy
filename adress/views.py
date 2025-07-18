from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from adress.serializers import AdressSerializer
from adress.models import Adress

class AdressCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Adress.objects.all()
    serializer_class= AdressSerializer

class AdressRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = (IsAuthenticated,)
        queryset=Adress.objects.all()
        serializer_class= AdressSerializer
