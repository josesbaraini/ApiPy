
from django.contrib import admin
from django.urls import path
from adress.views import AdressCreateListView, AdressRetriveUpdateDestroyView
from client.views import ClientCreateListView, ClientRetriveUpdateDestroyView
from phone.views import PhoneCreateListView, PhoneRetriveUpdateDestroyView
from emails.views import EmailCreateListView, EmailRetriveUpdateDestroyView




urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('adresses/', AdressCreateListView.as_view(), name='adress'),
    path('adresses/<int:pk>/', AdressRetriveUpdateDestroyView.as_view(), name='adress-datails-view'),

    path('clients/', ClientCreateListView.as_view(), name='client'),
    path('clients/<int:pk>/', ClientRetriveUpdateDestroyView.as_view(), name='client-datails-view'),

    path('emails/', EmailCreateListView.as_view(), name='email'),
    path('emails/<int:pk>/', EmailRetriveUpdateDestroyView.as_view(), name='email-datails-view'),

    path('phones/', PhoneCreateListView.as_view(), name='phone'),
    path('phones/<int:pk>/', PhoneRetriveUpdateDestroyView.as_view(), name='phone-datails-view'),


]
