from rest_framework import generics
from emails.models import Email
from emails.serializers import EmailSerializer


# Create your views here.
class EmailCreateListView(generics.ListCreateAPIView):
    queryset=Email.objects.all()
    serializer_class = EmailSerializer

class EmailRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Email.objects.all()
    serializer_class = EmailSerializer