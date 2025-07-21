import csv
from django.core.management.base import BaseCommand
from adress.models import Adress


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help="Nome do arquivo com endereços"
        )

    def handle(self, *arg, **options):

        file_name = options["file_name"]

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                type = row['type']
                state_registration = row['state_registration']
                postal_code = row['postal_code']
                address = row['address']
                address_complement = row['address_complement']
                neighborhood = row['neighborhood']
                city = row['city']
                area_code = row['area_code']
                state_abbr = row['state_abbr']
                state = row['state']
                ibge_code = row['ibge_code']
                
                Adress.objects.create(
                type = type,
                state_registration = state_registration,
                postal_code = postal_code,
                address = address,
                address_complement = address_complement,
                neighborhood = neighborhood,
                city = city,
                area_code = area_code,
                state_abbr = state_abbr,
                state = state,
                ibge_code = ibge_code
                )
