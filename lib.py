# You don't have to use these classes, but we recommend them as a good place to start!
import requests
from dotenv import load_dotenv
import os

load_dotenv()

class MongoHandler():
    pass

class WeatherGetter():
    def __init__(self):
        self.BASE_URL = 'https://api.darksky.net/'
        self.SECRET_KEY = os.getenv("DARKSKY_KEY")
        
    def weather_getter(self):
        forcast = requests.get(f"{self.BASE_URL}forecast/{self.SECRET_KEY}/%s,%s")
        return forcast