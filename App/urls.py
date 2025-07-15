
from django.contrib import admin
from django.urls import path
from adress.views import adress_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adresses/', adress_view, name='adress'),


]
