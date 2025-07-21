from django.db.models import Count, Avg
from rest_framework import generics, response
from rest_framework.permissions import IsAuthenticated
from rest_framework import views
from client.models import Client
from client.serializers import ClientModelSerializer
from App.permisions import GlobalPermissionClass
from reviews.models import Review


class ClientCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset = Client.objects.all().prefetch_related('emails')
    serializer_class = ClientModelSerializer


class ClientRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset = Client.objects.prefetch_related('emails').all()
    serializer_class = ClientModelSerializer


class ClientStatsView(views.APIView):
    queryset = Client.objects.all()
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)

    def get(self, request):

        total_clients = Client.objects.count()
        clients_by_type = Client.objects.values('type').annotate(count=Count('id'))
        total_review = Review.objects.count()
        avarege_stars = Review.objects.aggregate(Avg('stars'))['stars__avg']

        return response.Response(
            data={
                'total_clients': total_clients,
                'clients_by_type': clients_by_type,
                'total_review': total_review,
                'avarege_stars': round(avarege_stars) if avarege_stars else 0
            })
