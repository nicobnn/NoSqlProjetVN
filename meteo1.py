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
    params3 = {
            'access_key': '547d7636a660c07121e7200da3f50b89',
            'query': 'New York',
            }
    params4 = {
            'access_key': '547d7636a660c07121e7200da3f50b89',
            'query': 'Tokyo',
            }
    params5 = {
            'access_key': '547d7636a660c07121e7200da3f50b89',
            'query': 'Sydney',
            }
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_result2 = requests.get('http://api.weatherstack.com/current', params2)
    api_result3 = requests.get('http://api.weatherstack.com/current', params3)
    api_result4 = requests.get('http://api.weatherstack.com/current', params4)
    api_result5 = requests.get('http://api.weatherstack.com/current', params5)
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
    data3 = json.loads("[" + api_result3.text+"]")
    data4 = json.loads("[" + api_result4.text+"]")
    data5 = json.loads("[" + api_result5.text+"]")
    print(data,data2,data3,data4,data5)
    db = client.meteo
    paris = db.paris
    london = db.london
    new_york = db.new_york
    tokyo = db.tokyo
    sydney = db.sydney
    
    for x1 in data :
        paris.insert_one(x1)

    for x2 in data2 :
        london.insert_one(x2)
    
    for x3 in data3 :
        new_york.insert_one(x3)
    
    for x4 in data4 :
        tokyo.insert_one(x4)
    
    for x5 in data5 :
        sydney.insert_one(x5)
           
    client.close()
    

    #print(api_response)
    


def foo():
  pushtoMongo()
  

while True:
  foo()
  time.sleep(360)

