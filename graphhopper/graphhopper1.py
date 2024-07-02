import requests
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"
loc1 = "Santiago."
loc2 = "Buenos Aires"
key = "23acfbcf-1852-4285-9b6c-1be48198c426"

url = geocode_url + urllib.parse.urlencode ({"q": loc1, "limit": "1", "key": key})

replydata = requests.get(url)
json_data = replydata.json()
json_status = replydata.status_code
print(json_data)