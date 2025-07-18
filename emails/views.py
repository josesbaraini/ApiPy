from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from emails.models import Email
from emails.serializers import EmailSerializer


# Create your views here.
class EmailCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Email.objects.all()
    serializer_class = EmailSerializer

class EmailRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Email.objects.all()
    serializer_class = EmailSerializer