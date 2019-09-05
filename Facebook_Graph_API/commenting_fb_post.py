import fb #To install this package run: sudo pip install fb
from facepy import GraphAPI #To install this package run: sudo pip install facepy
import facebook 
import time
 
 
token="EAACEdEose0cBAHUnxmGE7IZB3CWiaXHyGZBuvZAtsCa3jqlRgAGOgyzPNceZBTZAx36NX58j0CSQDK2UNHwGKZBQy4HL89WEkRt2uiaRGpkKZAbnKJ14y3KhLruIOnZBWwfxOZBo1TpD37LtteZBxkgm6itIOLap7I3TP5GR1mstsUjpCF5GbMXxx7bSFr3J4uue2WmZAcO1HaqWsGbpKfEg2qeWzidJpih5VijpDbRXzYVDQZDZD"#Insert access token here.  
facebook1=fb.graph.api(token)
graph1 = GraphAPI(token)
 
graph = facebook.GraphAPI("EAACEdEose0cBAHUnxmGE7IZB3CWiaXHyGZBuvZAtsCa3jqlRgAGOgyzPNceZBTZAx36NX58j0CSQDK2UNHwGKZBQy4HL89WEkRt2uiaRGpkKZAbnKJ14y3KhLruIOnZBWwfxOZBo1TpD37LtteZBxkgm6itIOLap7I3TP5GR1mstsUjpCF5GbMXxx7bSFr3J4uue2WmZAcO1HaqWsGbpKfEg2qeWzidJpih5VijpDbRXzYVDQZDZD") 
vid=652034631542341 #This is IRSC page's facebook id
query=str(vid)+"/posts?fields=id&limit=1"
r=graph1.get(query)
 
 
 
idlist=[x['id'] for x in r['data']]
print("There are "+ str(len(idlist)) +" commentable posts.")
print(idlist) 
char1='y'
count=0
if char1=='y':
    nos=input("Enter number of posts to be commented on: ")
    nos=int(nos)
    if int(nos)<=len(idlist):
       for indid in idlist:
           
           
    	   count=count+1
    	   print("Hi")
    	   graph.put_object(parent_object=indid, connection_name='comments',message='First!')
    	   graph.put_object(indid, "comments", message="Wow")
    	   facebook1.publish(cat="comments",id=indid,message="Wow.."+str(count))
    	   time.sleep(6)
    	   print("Complaint number:"+str(count)+" on www.facebook.com/"+str(indid).split('_')[0]+"/posts/"+str(indid).split('_')[1])
           
	   
	  
          
           	  
    else: 
          print("Not that many commentable posts available. ")
else :
  print("No complaints made.")
