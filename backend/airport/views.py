from django.http import HttpResponse
from . import notam_service
import json 

# Create your views here.
def render(request):
    departure = request.GET['departure']
    print(f'Departure airport: {departure}')

    destination = request.GET['destination']
    print(f'Destination airport: {destination}')
    
    notams = notam_service.get_notams(departure, destination)
    return HttpResponse(json.dumps(notams), content_type="application/json")