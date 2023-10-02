from django.http import HttpResponse
from . import notam_service
import json 

# Create your views here.
def render(request):
    location = request.GET['location']
    print(location)
    page_size = request.GET['pageSize']
    print(page_size)
    notams = notam_service.get_notams(location, page_size)
    return HttpResponse(notams)