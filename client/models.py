from django.db import models
from adress.models import Adress


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    deleted = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    nickname = models.CharField(max_length=200)
    cpf = models.CharField(max_length=19)
    type = models.CharField(
        max_length=2,
        choices=[('PF', 'Individual'), ('PJ', 'Company')],
        default='PF'
    )
    general_registry = models.CharField(max_length=15, null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    adresses = models.ManyToManyField(Adress, related_name='clients')

    def __str__(self):
        return self.name
