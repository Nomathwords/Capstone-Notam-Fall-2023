import pip._vendor.requests as requests
from . import credentials, csv_parser, lat_long_shifting

api_url = "https://external-api.faa.gov/notamapi/v1/notams?"
headers =  {"Content-Type":"application/json", "client_id": credentials.client_id, 
                "client_secret": credentials.client_secret}

# Number of notams per page when API endpoint is hit
PAGE_SIZE = 200

def get_notams(departure_airport, destination_airport):
     
    # Get lat/longs of dep and dest airports 
    dep_lat, dep_long, dest_lat, dest_long = csv_parser.get_lat_long(departure_airport, destination_airport)
        
    # Get depature notams
    notams = retrieve_location_notams(departure_airport)
    
    # Get lat/longs between dep and dest airports 
    lat_longs_between = lat_long_shifting.calculate_next_coordinate(dep_lat, dep_long, dest_lat, dest_long, 25)
    
    # Get all lat/long notams that are between dep and est airports
    for i in range(len(lat_longs_between)):
        if i > 0 and  i < (len(lat_longs_between)-1) :
            notams += retrieve_lat_long_notams(lat_longs_between[i][0], lat_longs_between[i][1])
    
    # Get destination_airport notams 
    notams += retrieve_location_notams(destination_airport)
    
    # Get GPS notams
    notams += retrieve_location_notams("GPS");
    
    #Get chart notams
    notams += retrieve_feature_notams("CHART")
    
    #Get special use airspace notams
    notams += retrieve_feature_notams("SPECIAL")
    
     #Get airspace notams
    notams += retrieve_feature_notams("AIRSPACE")

    # Possibly consolidate this code into a function later
    notams_length = len(notams)

    # Add tags to the NOTAMs
    for i in range(0, notams_length):
        if notams[i]['properties']['coreNOTAMData']['notam']['classification'] == 'MIL':
            notams[i]["CS4273_SRC"] = "MIL"

        elif notams[i]['properties']['coreNOTAMData']['notam']['classification'] == 'FDC':
            notams[i]["CS4273_SRC"] = "FDC"

        elif notams[i]['properties']['coreNOTAMData']['notam']['location'] == 'GPS':
            notams[i]["CS4273_SRC"] = "GPS"

        else:
            notams[i]["CS4273_SRC"] = "General"

    return notams

def retrieve_location_notams(location):
    print(f'Getting notams from {location}')

    # Get the first response
    params = {"domesticLocation": location, "pageSize": PAGE_SIZE}
    response = query_notam_api(params)
    
    # Retrieve total number of pages and first list of notams
    total_pages = response.json()['totalPages']
    page_num = 1
    print(total_pages)
    print("Getting notams from page ", page_num)
    notams = response.json()['items']
    
    # Is there only one page of notams?
    if total_pages==1:
        return notams
    
    # More than one page
    page_num += 1 

    # Retrieve the rest of the notams 
    while page_num < (total_pages+1):
        print("Getting notams from page ", page_num)
        params = {"domesticLocation": location, "pageSize": PAGE_SIZE, "pageNum": int(page_num)}
        notams += query_notam_api(params).json()['items']
        page_num += 1

    return notams

def retrieve_lat_long_notams(latitude, longitude):
    print(f'Getting notams from coordinate ({latitude},{longitude})')

    # Get the first response
    params = {"locationLatitude": latitude, "locationLongitude": longitude, "locationRadius": 40, "pageSize": PAGE_SIZE}
    response = query_notam_api(params)
    
    # Retrieve total number of pages and first list of notams
    total_pages = response.json()['totalPages']
    page_num = 1
    print("Getting notams from page ", page_num)
    notams = response.json()['items']
    
    # Is there only one page of notams?
    if total_pages == 1:
        return notams
    
    # More than one page
    page_num += 1

    # Retrieve the rest of the notams 
    while page_num < (total_pages+1):
        print(f'Getting notams from page {page_num}')
        params = {"locationLatitude": latitude, "locationLongitude": longitude, "locationRadius": 40, "pageSize": PAGE_SIZE, "pageNum": int(page_num)}
        notams += query_notam_api(params).json()['items']
        page_num += 1

    return notams

def retrieve_feature_notams(feature):
    print(f'Getting {feature} notams')

    # Get the first response
    params = {"featureType": feature, "pageSize": PAGE_SIZE}
    response = query_notam_api(params)
    
    # Retrieve total number of pages and first list of notams
    total_pages = response.json()['totalPages']
    page_num = 1
    notams = response.json()['items']
    
    # Is there only one page of notams?
    if total_pages == 1:
        return notams
    
    # More than one page
    page_num += 1

    # Retrieve the rest of the notams 
    while page_num < (total_pages+1):
        print(f'Getting notams from page {page_num}')
        params = {"featureType": feature, "pageSize": PAGE_SIZE, "pageNum": int(page_num)}
        notams += query_notam_api(params).json()['items']
        page_num += 1

    return notams
    
# Hit FAA api
def query_notam_api(params):
    response = requests.get(api_url, headers=headers, params=params)
    return response