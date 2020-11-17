import os,requests 
from dotenv import load_dotenv
load_dotenv()

# Function to extract the desire requirement
def find(query, token=None, maximum = 50):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "key": os.getenv("GOOGLE_KEY"),
        "query": query
        }
    if token:
        params["pagetoken"] = token
    res = requests.get(url, params=params).json()
    results = res["results"]
    if 'next_page_token' in res.keys():
        token = res['next_page_token']
        r=[results, token]
    else: 
        r=[results,False]
    ubis = []
    token = None
    
    while len(ubis) < maximum:
        results, token = r
        ubis += results
        if not token: 
            break
    return ubis



# Function to extract the location:
def search(place,quantity):
    r = find(query=place, maximum = quantity)
    ad=[]
    latlng_str=[]
    latlng_lst=[]
    for i in range(len(r)):
        #ad.append(r[i]['formatted_address'])
        lat = r[i]['geometry']['location']["lat"]
        lng = r[i]['geometry']['location']["lng"]
        latlng_str.append(f"{lat},{lng}")
        latlng_lst.append([lat,lng])
    return latlng_str,latlng_lst



