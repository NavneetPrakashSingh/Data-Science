# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 16:49:15 2017

@author: Navneet
"""
import json
import requests
from pprint import pprint

#Application name	Demo
#API key	2545ecbfe616d68ff7a72242824fa09f
#Shared secret	bc949ee26d8bffa25fc4e122e8888b27
#Registered to	NaveetSingh
#http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=2545ecbfe616d68ff7a72242824fa09f&artist=Rihanna&album=Loud&format=json
url='http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=2545ecbfe616d68ff7a72242824fa09f&format=json'
data=requests.get(url).text
data=json.loads(data)
pprint(data["topartists"]["artist"][0]["name"])

