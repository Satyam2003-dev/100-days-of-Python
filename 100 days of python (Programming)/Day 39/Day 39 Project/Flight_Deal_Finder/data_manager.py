
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/********************/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data = {}
    
    def get_destination_data(self):
        '''Return travel destination data list of dictionaries'''
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        '''In case of blank IATA codes, this will update IATA code in google sheet'''
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
