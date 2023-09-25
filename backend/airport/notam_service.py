import pip._vendor.requests as requests
from . import credentials

api_url = "https://external-api.faa.gov/notamapi/v1/notams?"
headers =  {"Content-Type":"application/json", "client_id": credentials.client_id, 
                "client_secret": credentials.client_secret}
 
def get_notams(location, page_size):
    
    #Get the first response
    params = {"domesticLocation": location, "pageSize": int(page_size)}
    response = query_notam_api(params)
    
    #Retireve total number of pages and first list of notams
    total_pages = response.json()['totalPages']
    notams = response.json()['items']
    
    #Is there only one page of notams
    if total_pages==1:
        return notams
    
    page_num=2
    #Retrieve the rest of the notams 
    while page_num < (total_pages+1):
        print("Getting notams from page ", page_num)
        params = {"domesticLocation": location, "pageSize": int(page_size), "pageNum": int(page_num)}
        notams += query_notam_api(params).json()['items']
        page_num+=1
    return notams

#Hit FAA api
def query_notam_api(params):
    response = requests.get(api_url, headers=headers, params=params)
    return response