from django.http import JsonResponse
from adress.models import Adress
import json
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def adress_create_list_view(request):
    if request.method == 'GET':
        adresses = Adress.objects.all()
        date = [{'id':adress.id,'type':adress.type, 'state_registration':adress.state_registration,'postal_code':adress.postal_code, 'address':adress.address} for adress in adresses]
        return JsonResponse(date, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_adress = Adress.objects.create(
            type=data['type'],  
            state_registration=data['state_registration'],
            postal_code=data['postal_code'],
            address=data['address'],
            address_complement = data['address_complement'],
            neighborhood = data['neighborhood'],
            city = data['city'],
            area_code = data['area_code'],
            state_abbr = data['state_abbr'],
            state = data['state'],
            ibge_code = data['ibge_code'],
        )
        new_adress.save()
        return JsonResponse(
            {'id':new_adress.id, 'adress': new_adress.address}, status=201
        )
@csrf_exempt
def adress_datail_view(request, pk):
    adress = get_object_or_404(Adress, pk=pk)
    if request.method == 'GET':
        date = {
        'id': adress.id,
        'type': adress.type,
        'state_registration': adress.state_registration,
        'postal_code': adress.postal_code,
        'address': adress.address,
        'address_complement': adress.address_complement,
        'neighborhood': adress.neighborhood,
        'city': adress.city,
        'area_code': adress.area_code,
        'state_abbr': adress.state_abbr,
        'state': adress.state,
        'ibge_code': adress.ibge_code
    }
        return JsonResponse(date)
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        adress.type=data['type']
        adress.state_registration=data['state_registration']
        adress.postal_code=data['postal_code']
        adress.address=data['address']
        adress.address_complement = data['address_complement']
        adress.neighborhood = data['neighborhood']
        adress.city = data['city']
        adress.area_code = data['area_code']
        adress.state_abbr = data['state_abbr']
        adress.state = data['state'],
        adress.ibge_code = data['ibge_code']
        adress.save()

        return JsonResponse(
            {'id':adress.id, 'adress': adress.address}
        )