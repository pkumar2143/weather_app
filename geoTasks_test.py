from geoTasks import *

list_of_locations = ["Philadelphia, PA", "Hanover, MD", "Columbus, OH", "West Point, NY", "US Naval Academy"]

for location in list_of_locations:
    print(f"-------- {location} ---------")
    loc, address, (lat, lon) = find_address_gps(location)
    # Finding data types produced
    print(f"Loc type = {type(loc)}")          # geopy.location.Location
    print(f"Address type = {type(address)}")  # str
    print(f"Lat type = {type(lat)}")          # float
    print(f"Lon type = {type(lon)}")          # float
    print("\n")