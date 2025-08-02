# Collection of all classes to be used for collecting and organizing data
from geopy.geocoders import Nominatim

class DataHunter:
    pass

class LocationHunter(DataHunter):
    def __init__(self, textLocation):
        self.textLocation = textLocation
        self._geolocator  = Nominatim(user_agent="weather_app")
        self._location    = self._geolocator.geocode(self.textLocation)
        self._latitude    = self._location.latitude
        self._longitude   = self._location.longitude

    ## Create getter-setter methods 

class PropertiesHunter(DataHunter):
    def __init__(self, textLocation):
        self.textDescription
        self.temperature

    ## Create getter-setter methods 