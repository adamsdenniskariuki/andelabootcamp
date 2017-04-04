# http client to consume a public API

from urllib.request import urlopen, Request, HTTPError
import json

def http_client(url):
    
    request = Request(url)
    
    try:
        response = urlopen(request)
        output = json.loads(response.read().decode('utf-8'))
        
    except HTTPError as error:
        return 'Error connecting to the API:', error
        
    else:
        return output['city']['country']
    
# Open Weather API
print(http_client('http://api.openweathermap.org/data/2.5/forecast/daily?q=Nairobi&APPID=9e68c31e59d752247d58d439c50aaaff'))

"""

Another example call to the NASA API

print(http_client('https://api.nasa.gov/planetary/apod?api_key=iQ4eh40kqXhUlqeH480pMjR54TQXDY1ZU2FV7Bct'))

"""