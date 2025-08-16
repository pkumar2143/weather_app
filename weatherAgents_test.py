from weatherAgents import *

list_of_locations = ["Philadelphia, PA", "Hanover, MD", 
                     "Columbus, OH", "West Point, NY", 
                     "US Naval Academy"]

for location in list_of_locations:
    print(f"\n ----- {location} ----- ")
    hunter1 = LocationHunter(location)

    #print(hunter1.geolocator)
    print(f">>> LOCATION = {hunter1.location}")
    print(f">>> LATITUDE = {hunter1.latitude}")
    print(f">>> LONGITUDE = {hunter1.longitude}")
    print(f">>> NEAREST OBS STATION CALL = {hunter1.nearest_obs_st}")

    # Should not be accessed in such a manner
    #print(hunter1._location)
    #print(hunter1._latitude)
    #print(hunter1._longitude)