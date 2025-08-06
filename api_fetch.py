# Fetching National Weather Service Data

import requests
import json

base_url = "https://api.weather.gov/"
call_url = "https://api.weather.gov/points/39.9526,-75.1652"

zoneID_PHL = "PAC101" # not right...
lat_lon_phl = "39.9526,-75.1652"

psu_fzoneID = "PAZ019" # Arboretum @ PSU
psu_lat_lon = "40.80642,-77.86902"
psu_station_id = "KUNV"

def find_nearest_obs_station(lat, lon):
    api_call = f"https://api.weather.gov/points/{lat},{lon}"
    try:
        response = requests.get(api_call)

        if response.status_code == 200:
            print("...Successful Call...")
            return response.json()
        else:
            print(f"Error:{response.status_code}")
            return None
    except:
        print("There was a BIG BAD ERROR!!!")


def get_observation():
    final_call = base_url + "zones/forecast/"+psu_fzoneID+"/observations"
    try:
        print(f"Trying call: {final_call}")
        response = requests.get(final_call)

        if response.status_code == 200:
            print("Success!")
            posts = response.json()
            return posts
            print(posts)
        else:
            print(f"Error:{response.status_code}")
            return None
    except:
        print("There was a BIG ERROR!!!")

def get_properties():
    posts = get_observation()
    #posts_json = json.dumps(posts)
    properties = posts['properties']
    
    textDescription = properties['textDescription']
    temperature = properties['temperature']['value']
    windDirection = properties['windDirection']['value']
    windSpeed =  properties['windSpeed']['value']

    return properties, textDescription, temperature, windDirection, windSpeed