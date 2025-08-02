from weatherAgents import *

list_of_locations = ["Philadelphia, PA", "Hanover, MD", "Columbus, OH", "West Point, NY", "US Naval Academy"]

for location in list_of_locations:
    print(f"\n ----- {location} ----- ")
    hunter1 = LocationHunter(location)
    print(hunter1._location)
    print(hunter1._latitude)
    print(hunter1._longitude)