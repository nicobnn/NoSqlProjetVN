import requests
import json
from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)
db = client.meteo
paris = db.paris
london = db.london
new_york = db.new_york
tokyo = db.tokyo
sydney = db.sydney
client.close()

def meteolive(collection):
    mydoc = collection.find().sort("_id", -1).limit(1)
    for x in mydoc:
        pprint.pprint(x)

print("Que voulez vous faire ?")
print("1 - live meteo")
print()
print("Appuyez sur 1, 2,3 ou 4")
choice=input()

if(choice =='1'):
    print("Choisisssez la ville:")
    print("1-Paris")
    print("2-Londres")
    print("3-Sydney")
    print("4-New-York")
    print("5-Tokyo")
    choice2=input()
    if(choice2=='1'):
        meteolive(paris)
    if(choice2=='2'):
        meteolive(london)
    if(choice2=='3'):
        meteolive(sydney)
    if(choice2=='4'):
        meteolive(new_york)
    if(choice2=='5'):
        meteolive(tokyo)
