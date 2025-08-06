import requests
from api_fetch import *

psu_lat_lon = (40.80642,-77.86902)
lat_lon_phl = (39.9526,-75.1652)

response_body = find_nearest_obs_station(psu_lat_lon[0], psu_lat_lon[1])
print("---- Response Body ---- \n", response_body)

properties = response_body['properties']
print(" >>> Properties:\n", properties)

obs_station_call = properties['observationStations']
print(" >>> Properties:\n", obs_station_call)

try:
    response = requests.get(obs_station_call)
    print("Success")
except:
    print("Nope!")

print(response.json())

### Note: Going to have to go in a weird circle.
# Use lat-lon to make api call to get the observation station.
# Select some observation station, but make sure it can be successfully reached, if not select the next.
# FInd the weather observations you want.