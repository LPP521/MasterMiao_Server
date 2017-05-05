from django.http import HttpResponseNotFound
from django.http import JsonResponse

from models.location import LocationLog


def query(request):
    if request.method != 'GET':
        return HttpResponseNotFound()
    if not 'filter' in request.GET:
        return HttpResponseNotFound()
    if request.GET['filter'] == 'all':
        locations = LocationLog.objects.all()
        location_list = []
        for loc in locations:
            location_list.append({
                'time': loc.date,
                'latitude': loc.latitude,
                'longitude': loc.longitude
            })
        return JsonResponse({'n': len(location_list), 'l': location_list})
    return HttpResponseNotFound
