'''
ISS Space Station location
http://open-notify.org/Open-Notify-API/ISS-Location-Now/
http://api.open-notify.org/iss-now.json
'''

import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response) #<Response [200]> - Response Code

# if response.status_code == 404:
#     raise Exception("The resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data.")
'''Instead of us raising status code errors can use this'''
response.raise_for_status()

data_json = response.json()
print(f"response.json(): {data_json}")
iss_position_dict = data_json["iss_position"]
longitude = iss_position_dict["longitude"]
latitude = iss_position_dict["latitude"]
print(f"iss_position: {iss_position_dict}")
print(f"Longitude: {longitude}")
print(f"Latitude: {latitude}")
