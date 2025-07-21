from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('adress.urls')),

    path('api/v1/', include('client.urls')),

    path('api/v1/', include('emails.urls')),

    path('api/v1/', include('phone.urls')),

    path('api/v1/', include('reviews.urls')),

    path('api/v1/', include('authentication.urls')),]
