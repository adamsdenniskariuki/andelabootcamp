# http client to consume a public API

import urllib2

def http_client(url):
    
    request = urllib2.Request(url)
    
    try:
        response = urllib2.urlopen(request)
        output = response.read()
        
    except urllib2.URLError, error:
        return 'Error connecting to the weather API:', 
        
    else:
        return output
    
# Open Weather API
print(http_client('http://api.openweathermap.org/data/2.5/forecast/daily?q=Nairobi&APPID=9e68c31e59d752247d58d439c50aaaff'))

# NASA API
print(http_client('https://api.nasa.gov/planetary/apod?api_key=iQ4eh40kqXhUlqeH480pMjR54TQXDY1ZU2FV7Bct'))