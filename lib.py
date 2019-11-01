# You don't have to use these classes, but we recommend them as a good place to start!
import requests
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

class MongoHandler():
    
    def __init__(self, dbname,div):
        self.myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.db = self.myclient[dbname]
        self.collection= self.db[div]

   
   
    
    def create_doc(self, team_name, total_goals, total_wins, win_percentage):
        dic={}
        dic['Team_Name']= team_name 
        dic['total_goals']= total_goals
        dic['total wins']= total_wins
        dic['win_percentage']= win_percentage
        return self.collection.insert_one(dic)


class WeatherGetter():
    def __init__(self, time = None):
        self.BASE_URL = 'https://api.darksky.net/'
        self.SECRET_KEY = os.getenv("DARKSKY_KEY")
        self.time = time
        
        
    def weather_getter(self, time):
        forcast = requests.get(f"{self.BASE_URL}forecast/{self.SECRET_KEY}/52.5200,13.4050,{time}?exclude=minutely,hourly,daily,alerts,flags")
        return forcast