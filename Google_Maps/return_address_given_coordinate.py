from xlrd import open_workbook
from xlwt import Workbook
import json,urllib.request
import requests
import math												#NAME OF INPUT FILE CONTAINING ONE SHEET
import re	
def Address(latitude,longitude):														#Function to return address of the given coordinates
    sensor = 'true'
    base = "http://maps.googleapis.com/maps/api/geocode/json?"
    params = "latlng={lat},{lon}&sensor={sen}".format(
        lat=latitude,
        lon=longitude,
        sen=sensor
    )
    url = "{base}{params}".format(base=base, params=params)      #getting the address of that coordinates
    response = requests.get(url)
    return response.json()['results'][0]['formatted_address']    #returnin the address
def checkdelhi(address):														#Funtion to check of the given address contains the word Delhi
    delhi = re.compile(r'Delhi')       #using regex class we will search for the word 'Delhi'
    matchObj = delhi.search(address)   #searhching the address
    if matchObj:
      return True
    else:
      return False
	
print(checkdelhi(Address(28.545906,77.198281)))		

	