import requests
import json
from pymongo import MongoClient
import pprint
from bson.son import SON

client = MongoClient('localhost', 27017)
db = client.meteo
paris = db.paris
london = db.london
new_york = db.new_york
tokyo = db.tokyo
sydney = db.sydney
lyon=db.lyon
marseille=db.marseille


#pprint.pprint(Paris.find_one())

#for post in Paris.find():
#    pprint.pprint(post)

#Paris.find().sort({_id:-1}).limit(10)

#Paris.find().sort({_id:-1}).limit(1)

#pprint.pprint(paris.find_one({"_id": -1}))



def meteolive(collection):
    mydoc = collection.find().sort("_id", -1).limit(1)
    for x in mydoc:
        pprint.pprint(x)

def last_temperature(collection):
    mydoc = collection.find().sort("_id", -1).limit(1)
    array = list(mydoc)
    temp= array[0]["current"]["temperature"]
    name= array[0]["location"]["name"]
    return [temp,name]

def lastUV(collection):
    mydoc = collection.find().sort("_id", -1).limit(1)
    array = list(mydoc)
    temp= array[0]["current"]["uv_index"]
    name= array[0]["location"]["name"]
    return [temp,name]

def UVcity():
    tab=[0]*7
    tab[0]=lastUV(paris)
    tab[1]=lastUV(london)
    tab[2]=lastUV(sydney)
    tab[3]=lastUV(new_york)
    tab[4]=lastUV(tokyo)
    tab[5]=lastUV(lyon)
    tab[6]=lastUV(marseille)
    tab.sort()
    for i in range(7):
        print(tab[i])


def warmest_coolest():
    tab=[0]*7
    tab[0]=last_temperature(paris)
    tab[1]=last_temperature(london)
    tab[2]=last_temperature(sydney)
    tab[3]=last_temperature(new_york)
    tab[4]=last_temperature(tokyo)
    tab[5]=lastUV(lyon)
    tab[6]=lastUV(marseille)
    tab.sort()
    for i in range(7):
        print(tab[i])

'''
Afficher les villes qui ont le moins d'UV et les villes à éviter

Afficher toutes les villes où il fait beau/partiellement couvert : 'Partly cloudy'

Afficher la température moyenne d'une ville précise sur un jour

'''
ans=True
while ans:
    print("Nous avons des données sur ( villes différentes: paris, londres, sydney, new_york et tokyo.")
    print("Que voulez vous faire ?")
    print("1 -Meteo complete de la ville")
    print("2 -Afficher uniquement la dernière temperature de la ville")
    print("3 -Afficher la ville la plus chaude et la ville la plus froide(tri des villes suivant la temperature.")
    print("4 -Afficher uniquement le dernier indice UV de la ville")
    print("5 -Afficher la ville la plus exposé aux UB et la ville la moins exposé(tri des villes suivant l'indice uv.")
    print("10 -Quitter")
    print("Ecrivez sur la console le chiffre choisie")
    ans=input()
    if(ans =='1'):
        print("Choisisssez la ville:")
        print("1-Paris")
        print("2-Londres")
        print("3-Sydney")
        print("4-New-York")
        print("5-Tokyo")
        print("6-Lyon")
        print("7-Marseille")
        ville=input()
        if(ville=='1'):
            meteolive(paris)
        if(ville=='2'):
            meteolive(london)
        if(ville=='3'):
            meteolive(sydney)
        if(ville=='4'):
            meteolive(new_york)
        if(ville=='5'):
            meteolive(tokyo)
        if(ville=='6'):
            meteolive(lyon)
        if(ville=='7'):
            meteolive(marseille)
    elif(ans=='2'):
        print("Choisisssez la ville:")
        print("1-Paris")
        print("2-Londres")
        print("3-Sydney")
        print("4-New-York")
        print("5-Tokyo")
        print("6-Lyon")
        print("7-Marseille")
        ville2=input()
        if(ville2=='1'):
            print(last_temperature(paris))
        if(ville2=='2'):
            print(last_temperature(london))
        if(ville2=='3'):
            print(last_temperature(sydney))
        if(ville2=='4'):
            print(last_temperature(new_york))
        if(ville2=='5'):
            print(last_temperature(tokyo))
        if(ville2=='6'):
            print(last_temperature(lyon))
        if(ville2=='7'):
            print(last_temperature(marseille))
    elif(ans=='3'):
        warmest_coolest()
    elif(ans=='4'):
        print("Choisisssez la ville:")
        print("1-Paris")
        print("2-Londres")
        print("3-Sydney")
        print("4-New-York")
        print("5-Tokyo")
        print("6-Lyon")
        print("7-Marseille")
        ville3=input()
        if(ville3=='1'):
            print(lastUV(paris))
        if(ville3=='2'):
            print(lastUV(london))
        if(ville3=='3'):
            print(lastUV(sydney))
        if(ville3=='4'):
            print(lastUV(new_york))
        if(ville3=='5'):
            print(lastUV(tokyo))
        if(ville3=='6'):
            print(lastUV(lyon))
        if(ville3=='7'):
            print(lastUV(marseille))
    elif(ans=='5'):
        UVcity()
        
    elif(ans=='10'):
        print("\n Goodbye")
        ans=None
    else:
        print("\n Not Valide Choice Try again")
        
    
