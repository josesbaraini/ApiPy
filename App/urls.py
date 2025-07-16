
from django.contrib import admin
from django.urls import path
from adress.views import AdressCreateListView, AdressRetriveUpdateDestroyView
from client.views import ClientCreateListView, ClientRetriveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('adresses/', AdressCreateListView.as_view(), name='adress'),
    path('adresses/<int:pk>/', AdressRetriveUpdateDestroyView.as_view(), name='adress-datauls-view'),
    path('clients/', ClientCreateListView.as_view(), name='adress'),
    path('clients/<int:pk>/', ClientRetriveUpdateDestroyView.as_view(), name='adress-datauls-view'),


]
