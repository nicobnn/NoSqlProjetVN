"""
Created on Sat Mar  7 10:02:03 2020

@author: Nicolas
"""
import requests
import time
import json
from pymongo import MongoClient

def pushtoMongo():
    
    
    params = {
            'access_key': '547d7636a660c07121e7200da3f50b89',
            'query': 'Paris',
            }
    params2 = {
            'access_key': '547d7636a660c07121e7200da3f50b89',
            'query': 'London',
            }
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_result2 = requests.get('http://api.weatherstack.com/current', params2)
    '''
    #here we can print some values returned by the api
    print(u'Current meteo at %s is :' % (api_response['location']['name']))
    print(u'temperature = %d℃'  % (api_response['current']['temperature']))
    print(u'description = %s'  % (api_response['current']['weather_descriptions']))
    print(u'precipitation = %dmm'  % (api_response['current']['precip']))
    print(u'humidity in percentage = %d'  % (api_response['current']['humidity']))
    print(u'uv_index = %d'  % (api_response['current']['uv_index']))
    '''
    
    client = MongoClient('localhost', 27017)
    data = json.loads("[" + api_result.text+"]")
    data2 = json.loads("[" + api_result2.text+"]")
    print(data,data2)
    db = client.meteo
    col = db.test
    col2 = db.test2

    for x in data :
           col.insert_one(x)


    for z in data2 :
           col2.insert_one(z)

                
    client.close()
    
    #print(api_response)
    


def foo():
  pushtoMongo()
  

while True:
  foo()
  time.sleep(360)

