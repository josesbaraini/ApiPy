from django.db import models
from django.core.validators import RegexValidator

telefone_validator = RegexValidator(
    regex=r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$',
    message='Formato de telefone inválido. Exemplo: (11) 91234-5678'
)

class Phone(models.Model):
    id = models.AutoField(primary_key=True)

    phone = models.CharField(max_length=20, unique=True, null=True, validators=[telefone_validator])
    client = models.ForeignKey('client.client', on_delete=models.CASCADE, related_name='phones')

    def __str__(self):
        return self.phone
