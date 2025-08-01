from geoTasks import *

list_of_locations = ["Philadelphia, PA", "Hanover, MD", "Columbus, OH", "West Point, NY", "US Naval Academy"]

for location in list_of_locations:
    print(f"-------- {location} ---------")
    find_address_latlon(location)
    print("\n")