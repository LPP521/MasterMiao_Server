from django.http import HttpResponseNotFound, HttpResponse

from models.location import LocationLog


def delete(request):
    if request.method != 'GET':
        return HttpResponseNotFound()
    if not 'filter' in request.GET:
        return HttpResponseNotFound()
    if request.GET['filter'] == 'all':
        locations = LocationLog.objects.all()
        locations.delete()
        return HttpResponse('Success')
    return HttpResponseNotFound
