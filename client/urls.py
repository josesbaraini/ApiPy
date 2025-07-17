from django.urls import path
from . import views

urlpatterns = [

    path('clients/', views.ClientCreateListView.as_view(), name='client'),
    path('clients/<int:pk>/', views.ClientRetriveUpdateDestroyView.as_view(), name='client-datails-view'),



]