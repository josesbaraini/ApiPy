from django.urls import path
from . import views

urlpatterns = [
    path('emails/', views.EmailCreateListView.as_view(), name='email'),
    path('emails/<int:pk>/', views.EmailRetriveUpdateDestroyView.as_view(), name='email-datails-view'),



]