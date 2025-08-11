import requests
from api_fetch import *

# Testing entire API data pipeline.

psu_lat_lon = (40.80642,-77.86902)
lat_lon_phl = (39.9526,-75.1652)

# Find nearest Observation Station
response_body = find_nearest_obs_station(psu_lat_lon[0], psu_lat_lon[1])
print("---- Response Body ---- \n", response_body)

properties = response_body['properties']
print(" >>> Properties:\n", properties)

obs_station_call = properties['observationStations']
print(" >>> Stations within Gridpoint Call:\n", obs_station_call)

try:
    response = requests.get(obs_station_call)
    print("Success")
except:
    print("Nope!")

resp = response.json()
station_metadata = resp['features'][0]['properties']
obs_api_call_base = station_metadata['@id']
obs_api_call = obs_api_call_base + '/observations?limit=1' # only want 1 observation
print(f"Observation API Call = {obs_api_call}")

try:
    obs_response = requests.get(obs_api_call)
    print("Success")
except:
    print("Nope!")

obs_response_json = obs_response.json()
print(f"Observation Response = \n{obs_response_json}")
obs_response_json_props = obs_response_json['features'][0]['properties']
print(f"Observation properties = \n{obs_response_json_props}")
temp = obs_response_json_props['temperature']['value']
text_description = obs_response_json_props['textDescription']
print(f"Temperature = {temp} deg C, Text Description = {text_description}")

### Note: Going to have to go in a weird circle.
# Use lat-lon to make api call to get the observation station.
# Select some observation station, but make sure it can be successfully reached, if not select the next.
# FInd the weather observations you want.

#Date-time format for: 2025-08-11T21:53:00+00:00, ISO-8601