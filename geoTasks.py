# Geographic tasks for finding weather at certain locations. (Python library geopy may be of good use here...)
from geopy.geocoders import Nominatim

# Collect locations that user would enter (e.g. "Philadelphia, PA", "Hanover, MD")

list_of_locations = ["Philadelphia, PA", "Hanover, MD", "Columbus, OH"] # Starting small, can be "drop-down"-selected, or better "entry-completed"

# Find geo-tags (lat-lon, gridpoints, zipcodes)
def find_address_latlon(location):
    '''
    Find the address and GPS coordinates of any city.

    In: location, string of city or other location (like a landmark) (e.g. "Philadelphia, PA" or "Eiffel Tower, Paris")
    Out: 
    '''
    geolocator = Nominatim(user_agent="weather_app") # Replace with your application name
    location = geolocator.geocode(location)
    print(location)
    if location:
        print(f"Address: {location.address}")
        print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
        return location, location.address, (location.latitude, location.longitude)
    else:
        print("Location not found.")
        return None, None, None

# Find the nearest Forecast Zone and/or (Observation) Station




