"""

def http_client():
  
  import http.client
  connection = http.client.HTTPConnection("www.python.org", 80)
  connection.connect()
  connection.request("GET", "/")
  response = connection.getresponse()
  print (response.status, response.reason, response.read())
  connection.close()
  
http_client()

"""

import urllib2

def http_client(url):
    
    request = urllib2.Request(url)
    
    try:
        response = urllib2.urlopen(request)
        weather = response.read()
        
    except urllib2.URLError, error:
        return 'Error connecting to the weather API:', 
        
    else:
        return weather
    
print(http_client('http://api.openweathermap.org/data/2.5/forecast/daily?q=Nairobi&APPID=9e68c31e59d752247d58d439c50aaaff'))