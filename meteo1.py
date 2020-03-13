# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:02:03 2020

@author: Nicolas
"""
import requests
import time

def recupdonnees():
    params = {
            'access_key': '547d7636a660c07121e7200da3f50b89',
            'query': 'New York',
            }

    api_result = requests.get('http://api.weatherstack.com/current', params)

    api_response = api_result.json()


    #print(u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))
    print(api_response)
    
#recupdonnees()



def foo():
  recupdonnees()

while True:
  foo()
  time.sleep(20)

