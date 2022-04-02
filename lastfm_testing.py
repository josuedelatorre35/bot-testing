import mytokens
import os
import requests
import json
import xml.etree.ElementTree as ET
my_secret = mytokens.lfm_token

url3 = f'http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key={my_secret}&format=json'
 
query3 = {'user': 'tequileros97', 'limit': 10}

response3 = requests.get(url3, params = query3)
file3 = response3.json()

nice_file = json.dumps(file3, indent = 4, sort_keys= True)
print(nice_file)


for i in file3['artists']['artist']:
    print(i['name'], end=' ') #artist name
    print(f'(Plays: ', i['playcount'], ')', sep='') #playcount

