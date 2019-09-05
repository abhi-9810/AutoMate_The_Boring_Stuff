import facebook
import urllib
import urllib.request as urllib2
 
proxy = urllib2.ProxyHandler({'http': '127.0.0.1'})
auth = urllib2.HTTPBasicAuthHandler()
opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
urllib2.install_opener(opener)
 
graph = facebook.GraphAPI("EAACEdEose0cBAH3RFH8HmH3zxAmc4VovPc91yXzKUzHVkSBg7VqXhNIgj5cgtrEOsZA9RAdHYNkBJ3BMBzsZAZAe5UmubJE5BipxRjVGXetpJg7omAVUG89bAmRIGIuGch1y8gEcCb4ONhtM6VW23UixrcOOSbQupENBOYu1mmAqXBtOF8A3PT8scaDOYSC1ZBlxlB6ZA4QZDZD")
friends = graph.get_connections("me", "friends")
#friends = graph.get_object("me/friends")
for friend in friends['data']:
    print(friend)
    details = graph.get_connections(friend['id'],"")
    if 'birthday' in details.keys():
        print(friend['name'])
        print(details['birthday'])
