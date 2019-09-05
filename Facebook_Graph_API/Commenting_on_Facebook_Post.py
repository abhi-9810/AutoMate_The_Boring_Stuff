import facebook    #sudo pip install facebook-sdk
import itertools
import json
import re
import requests

access_token = "XXX"
user = '100003525263290'

graph = facebook.GraphAPI("EAACEdEose0cBAHUnxmGE7IZB3CWiaXHyGZBuvZAtsCa3jqlRgAGOgyzPNceZBTZAx36NX58j0CSQDK2UNHwGKZBQy4HL89WEkRt2uiaRGpkKZAbnKJ14y3KhLruIOnZBWwfxOZBo1TpD37LtteZBxkgm6itIOLap7I3TP5GR1mstsUjpCF5GbMXxx7bSFr3J4uue2WmZAcO1HaqWsGbpKfEg2qeWzidJpih5VijpDbRXzYVDQZDZD")
profile = graph.get_object(user)
print(profile['id'])
posts = graph.get_connections('me', 'posts',limit=5)
feed = graph.get_connections('me', 'feed', limit=1000)
#print(feed)
#print(posts)
Jstr = json.dumps(posts)
JDict = json.loads(Jstr)

count = 0
for i in JDict['data']:
    allID = i['id']
    print(allID)
    graph.put_object(allID, "comments", message="I am commenting on this pic!")
    print("commented!")
    try:
        allComments = i['comments']

        for a in allComments['data']:  
            count += 1
            print(a['message'])


    except:
        pass


print(count)
