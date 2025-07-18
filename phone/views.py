from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from phone.models import Phone
from phone.serializers import PhoneSerializer
from App.permisions import GlobalPermissionClass


# Create your views here.
class PhoneCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset=Phone.objects.all()
    serializer_class = PhoneSerializer

class PhoneRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset=Phone.objects.all()
    serializer_class = PhoneSerializer