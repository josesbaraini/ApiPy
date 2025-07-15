
from django.contrib import admin
from django.urls import path
from adress.views import adress_create_list_view, adress_datail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adresses/', adress_create_list_view, name='adress'),
    path('adresses/<int:pk>/', adress_datail_view, name='adress-datauls-view'),


]
