from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from adress.serializers import AdressSerializer
from adress.models import Adress
from App.permisions import GlobalPermissionClass



class AdressCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass, )
    queryset=Adress.objects.all()
    serializer_class= AdressSerializer

class AdressRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = (IsAuthenticated, GlobalPermissionClass)
        queryset=Adress.objects.all()
        serializer_class= AdressSerializer
