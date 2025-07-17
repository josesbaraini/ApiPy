from django.urls import path
from . import views

urlpatterns = [
    path('adresses/', views.AdressCreateListView.as_view(), name='adress'),
    path('adresses/<int:pk>/', views.AdressRetriveUpdateDestroyView.as_view(), name='adress-datails-view'),



]