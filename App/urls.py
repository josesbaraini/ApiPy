
from django.contrib import admin
from django.urls import path
from adress.views import AdressCreateListView, AdressRetriveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adresses/', AdressCreateListView.as_view(), name='adress'),
    path('adresses/<int:pk>/', AdressRetriveUpdateDestroyView.as_view(), name='adress-datauls-view'),


]
