import requests

url = "https://realty-in-us.p.rapidapi.com/properties/v2/list-sold"

querystring = {"offset":"0","limit":"500","city":"Forsyth","state_code":"MO","sort":"sold_date","prop_type":"single_family"}

headers = {
    'x-rapidapi-host': "realty-in-us.p.rapidapi.com",
    'x-rapidapi-key': "5df2060bd4mshfd0efe8cbfb4d49p110decjsn092a11aa539b"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)