# Collection of all classes to be used for collecting and organizing data
import requests
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
        self.locHunter = LocationHunter(textLocation=textLocation)
        self.__lat = self.locHunter.latitude                        # Consider not assigning a (protected) var for this and just use LocationHunter method.
        self.__lon = self.locHunter.longitude
        self.__api_base = "https://api.weather.gov/"
        self.__api_points = "points/"
        self.__callconstruct = self.__api_base + "zones/forecast/"++"/observations"
        self.__properties = self.get_properties()
        self.textDescription = ''
        self.temperature = -999

    ## Create getter-setter methods
    def get_observation(self):
        final_call = self.__callconstruct
        try:
            print(f"Trying call: {final_call}")
            response = requests.get(final_call)

            if response.status_code == 200:
                print("Successfully obtained observation")
                posts = response.json()
                return posts
            else:
                print(f"Error:{response.status_code}")
                return None
        except:
            print("There was a BIG ERROR!!!")

    def get_properties(self):
        posts = self.get_observation()
        properties = posts['properties']

        return properties

    def get_textDescription(self, properties):
        textDescription = properties['textDescription']

        return textDescription #, windDirection, windSpeed
    
    def get_temperature(self, properties):
        temperature = properties['temperature']['value']

        return temperature