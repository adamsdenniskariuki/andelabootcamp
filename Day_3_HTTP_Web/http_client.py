# http client to consume a public weather API

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