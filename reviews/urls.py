from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewCreateListView.as_view(), name='review'),
    path('reviews/<int:pk>/', views.ReviewRetriveUpdateDestroyView.as_view(), name='review-datails-view'),

]