import unittest
import urllib2
import json

from http_client import http_client

class HTTPClientTest(unittest.TestCase):
	
	def test_it_works(self):
		result = http_client('http://api.openweathermap.org/data/2.5/forecast/daily?q=Nairobi&APPID=9e68c31e59d752247d58d439c50aaaff')
		out = json.load(result)
		country = out['city']['country']
		self.assertEqual(country, 'KE', "Not working")
