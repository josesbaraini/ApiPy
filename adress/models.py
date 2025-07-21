from django.db import models


class Adress(models.Model):
    type = models.CharField(
        max_length=2,
        choices=[('MA', 'Main Adress'), ('AA', 'Alternative Adress')],
        default='MA'
    )
    state_registration = models.CharField(max_length=20, null=True, blank=True)
    postal_code = models.CharField(max_length=9)
    address = models.CharField(max_length=150, null=True, blank=True)
    address_complement = models.CharField(max_length=50, null=True, blank=True)
    neighborhood = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    area_code = models.CharField(max_length=3, null=True, blank=True)
    state_abbr = models.CharField(max_length=2, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    ibge_code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.address
