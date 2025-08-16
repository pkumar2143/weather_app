# Collection of all classes to be used for collecting and organizing data
import requests
from geopy.geocoders import Nominatim

class DataHunter:
    pass

class LocationHunter(DataHunter):
    def __init__(self, textLocation):
        self.textLocation    = textLocation
        self._geolocator     = Nominatim(user_agent="weather_app")
        self._location       = self._geolocator.geocode(self.textLocation)
        self._latitude       = self._location.latitude
        self._longitude      = self._location.longitude
        self._nearest_obs_st = self._find_nearest_obs_station(self._latitude, self._longitude)

    ## Create getter methods
    @property
    def geolocator(self):
        '''
        Returns geolocator object. Probably unnecessary...
        '''
        return self._geolocator

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
    
    @property
    def nearest_obs_st(self):
        '''
        Returns nearest observation station
        '''
        return self._nearest_obs_st

    # Setter methods may not make sense, since they should only change if we change locations.
    def _find_nearest_obs_station(self, lat=2, lon=1):
        api_call = f"https://api.weather.gov/points/{lat},{lon}"
        try:
            response = requests.get(api_call)

            if response.status_code == 200:
                print("...Successful Call...")
                response_json = response.json()
            else:
                print(f"Error:{response.status_code}")
                #return None
        except:
            print("There was a BIG BAD ERROR!!!")
        
        properties = response_json['properties']
        obs_station_call = properties['observationStations']

        try:
            response2 = requests.get(obs_station_call)
            print("Success")
        except:
            print("Nope!")

        resp = response2.json()
        station_metadata = resp['features'][0]['properties']
        obs_api_call_base = station_metadata['@id']
        obs_api_call = obs_api_call_base + '/observations?limit=1' # only want 1 observation

        return obs_api_call


class PropertiesHunter(DataHunter):
    def __init__(self, textLocation):
        self.locHunter       = LocationHunter(textLocation=textLocation)
        self.__lat           = self.locHunter.latitude                        # Consider not assigning a (protected) var for this and just use LocationHunter method.
        self.__lon           = self.locHunter.longitude
        self.__api_base      = "https://api.weather.gov/"
        self.__api_points    = "points/"
        self.__callconstruct = self.__api_base + "zones/forecast/"+"/observations"
        self.__properties    = self.get_properties()
        self.textDescription = ''
        self.temperature     = -999

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