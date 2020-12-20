'''In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/json?

Please run your program to find the place_id for this location:

University of Washington - Bothell'''

import urllib.request, urllib.parse
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_endpoint="http://py4e-data.dr-chuck.net/json?"
location=input('Enter location: ')
parameters={'key':42,'address':location}
url=api_endpoint+urllib.parse.urlencode(parameters)

data=urllib.request.urlopen(url,context=ctx).read().decode()
json_data=json.loads(data)

place_id=json_data['results'][0]['place_id']
print("Place id:",place_id)