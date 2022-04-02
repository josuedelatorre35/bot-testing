import mytokens
import os
import requests
import json
import xml.etree.ElementTree as ET
my_secret = mytokens.lfm_token

url_np = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=rj&api_key={my_secret}&format=json&nowplaying="true"'

#http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=rj&api_key=9a85d653c1a3cd100e170f5911615e98&format=json&nowplaying="true"

query = {'user': 'tequileros97', 'limit': 1} #this  will filter out information to only retreive information from a specific user
#limit value placed to 1 so it only recieves the last song played

response = requests.get(url_np, params = query) #params will get information from specific user
print(response.status_code) #if 200 is return it response was successful

file = response.json()
nice_file = json.dumps(file, indent = 4, sort_keys= True) #same as file but with indentation

entries = json.dumps(file, indent = 5, sort_keys= True) #information stored in 'recentracks' key, used to read json file more easily 

'''
print('print #1')
print()
print(file) #prints raw file


print()
print('print #2')
print()
print(entries) #prints 'recenttracks' key for json dictionary (indented)



print()
print('print #3')
print()
stuff = json.dumps(file['recenttracks']['track'], indent = 5, sort_keys= True)
print(stuff) #prints 'track' key in 'recenttracks' dictionary
'''


print()
print('actual useful stuff')
print()

'''1ST FUNCTION'''
'''Now playing function (only prints information. No bot commands)'''


#below is to print artist name (now playing)
counter1 = 0
for i in file['recenttracks']['track']:
  if counter1 == 0:
    print(i['artist']['#text'])
    counter1 += 1

#below is to print album name (now playing)
counter2 = 0
for i in file['recenttracks']['track']:
  if counter2 == 0:
    print(i['album']['#text'])
    counter2 += 1

#below is to print song name (now playing)
counter3 = 0
for i in file['recenttracks']['track']:
  if counter3 == 0:
    print(i['name'])
    counter3 += 1
    
#below is to print image url of album (now playing)
counter4 = 0
for i in file['recenttracks']['track']:
  if counter4 == 0:
    print(i['image'][2]['#text'])
    #'image' key contains a list, so get 3rd entry to retrieve large file url (by getting value for #text key)
    counter4 += 1

'''End of Funtion'''


'''2ND FUNCTION'''
'''Next function: Shows Top artists'''


url_2 = f'http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=rj&api_key={my_secret}&format=json'
query2 = {'user': 'tequileros97', 'limit': 5}


response2 = requests.get(url_2, params = query2)
file2 = response2.json()
nice_file2 = json.dumps(file, indent = 4, sort_keys= True)
artists = json.dumps(file2["topartists"]['artist'], indent = 4, sort_keys= True)
print(artists) #see what it prints

for i in file2["topartists"]['artist']:
    print(i['name'])
    print(f'Plays:', i['playcount'])
    print(i['url'])
    print()

'''End of Funtion'''


'''3RD FUNCTION'''
'''Shows Top albums'''

url3 = f'http://ws.audioscrobbler.com/2.0/?method=user.gettopalbums&user=rj&api_key={my_secret}&format=json'
 
query3 = {'user': 'tequileros97', 'limit': 5}

response3 = requests.get(url3, params = query3)
file3 = response3.json()

nice_file = json.dumps(file3, indent = 4, sort_keys= True)
print(nice_file)

for i in file3["topalbums"]['album']:
    print(i['name']) #album name
    print(i['artist']['name']) #artist name
    print(f'Plays:', i['playcount']) #playcount
    print(i['image'][2]['#text']) #image url
    print()
