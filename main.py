import json
import webbrowser
import os
from json2html import json2html
from requests import request
from config import APIKEY

city = input("Enter city: ")
state = input("Enter state code: ").capitalize()
radius = input("Enter radius: ")
year_built = input("Enter year built max: ")

url = "https://realty-in-us.p.rapidapi.com/properties/v2/list-sold"

querystring = {"offset": "0", "limit": "500", "city": city, "state_code": state, "sort": "sold_date",
               "prop_type": "single_family", "radius": radius}

headers = {
    'x-rapidapi-host': "realty-in-us.p.rapidapi.com",
    'x-rapidapi-key': APIKEY
}

response = request("GET", url, headers=headers, params=querystring)

properties = json.loads(response.text)["properties"]
property_count = 0
data_file = open('properties.html', 'w+')
properties_array = []
for item in properties:
    if item['year_built'] is None:
        continue
    if int(item['year_built']) < int(year_built):
        property_count += 1
        properties_array.append(item)
properties_array.sort(key=lambda x: x['year_built'])
data_file.write(f'<h1>Properties Found: {property_count}</h1>')
for item in properties_array:
    data_file.write(json2html.convert(json=item))
    data_file.write('<br><hr><br>')
data_file.close()
filename = f'file:///{os.getcwd()}/properties.html'
webbrowser.open_new_tab(filename)