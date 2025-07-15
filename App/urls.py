
from django.contrib import admin
from django.urls import path
from adress.views import AdressCreateListView, adress_datail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adresses/', AdressCreateListView.as_view(), name='adress'),
    path('adresses/<int:pk>/', adress_datail_view, name='adress-datauls-view'),


]
