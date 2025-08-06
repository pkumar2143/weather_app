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

    ## Create getter methods    
    @property
    def location(self):
        '''
        Returns full location information as in the NWS DB.
        Some info not available all the time (e.g. some locations have zipcodes, others do not.)
        Dtype str
        '''
        return self._location
    
    @property
    def latitude(self):
        '''
        Returns latitude of the user-desired location.
        Dtype float
        '''
        return self._latitude
    
    @property
    def longitude(self):
        '''
        Returns longitude of the user-desired location.
        Dtype float
        '''
        return self._longitude
    
    # Setter methods may not make sense, since they should only change if we change locations.


class PropertiesHunter(DataHunter):
    def __init__(self, textLocation):
        self.textDescription
        self.temperature

    ## Create getter-setter methods 