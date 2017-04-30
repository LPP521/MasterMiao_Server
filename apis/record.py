import datetime

from django.http import HttpResponse
from django.http import HttpResponseNotFound

from models.location import LocationLog


def record(request):
    if request.method != 'GET':
        return HttpResponseNotFound()
    if not 'latitude' in request.GET:
        return HttpResponseNotFound()
    if not 'longitude' in request.GET:
        return HttpResponseNotFound()
    latitude = 0
    longitude = 0
    try:
        latitude = float(request.GET['latitude'])
        longitude = float(request.GET['longitude'])
    except ValueError:
        return HttpResponseNotFound
    post_location = LocationLog(
        date=datetime.datetime.now(),
        latitude=latitude,
        longitude=longitude
    )
    post_location.save()
    return HttpResponse('Success')


def query(request):
    if request.method != 'GET':
        return HttpResponseNotFound()
    if not 'filter' in request.GET:
        return HttpResponseNotFound()
    if request.GET['filter'] == 'all':
        locations = LocationLog.objects.all()
        response = ''
        for loc in locations:
            response += loc.date + ' '
            response += loc.latitude + ' '
            response += loc.longitude + '\n'
        return HttpResponse(response)
    return HttpResponseNotFound
