from django.contrib import admin
from adress.models import Adress

@admin.register(Adress)
class AdressAdmin(admin.ModelAdmin):
    list_display = ('id','type', 'state_registration', 'postal_code', 'address',)

