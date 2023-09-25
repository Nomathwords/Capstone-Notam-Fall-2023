from django.http import HttpResponse
from . import notam_service

# Create your views here.
def render(request):
    departure = request.GET['departure']
    print("Departure airport: ", departure)
    destination = request.GET['destination']
    print("Destination airport: ", destination)
    notams = notam_service.get_notams(departure, destination)
    return HttpResponse(notams)