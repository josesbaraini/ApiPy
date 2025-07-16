from rest_framework import generics
from phone.models import Phone
from phone.serializers import PhoneSerializer


# Create your views here.
class PhoneCreateListView(generics.ListCreateAPIView):
    queryset=Phone.objects.all()
    serializer_class = PhoneSerializer

class PhoneRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Phone.objects.all()
    serializer_class = PhoneSerializer