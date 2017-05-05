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


