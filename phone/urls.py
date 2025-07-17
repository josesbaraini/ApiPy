from django.urls import path
from . import views

urlpatterns = [
    path('phones/', views.PhoneCreateListView.as_view(), name='phone'),
    path('phones/<int:pk>/', views.PhoneRetriveUpdateDestroyView.as_view(), name='phone-datails-view'),

]