from django.db import models
from adress.models import Adress
from django.core.validators import RegexValidator

telefone_validator = RegexValidator(
    regex=r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$',
    message='Formato de telefone inválido. Exemplo: (11) 91234-5678'
)

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
    

class Email(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True, null=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='emails')

    def __str__(self):
        return self.email

class Phone(models.Model):
    id = models.AutoField(primary_key=True)

    phone = models.CharField(max_length=20, unique=True, null=True, validators=[telefone_validator])
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='phones')

    def __str__(self):
        return self.phone