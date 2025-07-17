from django.db import models
from client.models import Client

# Create your models here.

class Review(models.Model):
    class StarsRateChoices(models.IntegerChoices):
        ZERO = 0, '0 estrelas'
        ONE= 1, '1 estrela'
        TWO = 2, '2 estrelas'
        THREE = 3, '3 estrelas'
        FOUR = 4, '4 estrelas'
        FIVE = 5, '5 estrelas'
    stars = models.IntegerField(choices=StarsRateChoices.choices)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='reviews')
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.client
    

