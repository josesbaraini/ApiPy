from django.db import models
from client.models import Client


class Email(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True, null=True)
    client = models.ForeignKey('client.client', on_delete=models.CASCADE, related_name='emails')

    def __str__(self):
        return self.email
