""" Manage the fetcher """
from os import getenv
import requests

API_TIMEOUT = 30

class BerryDataFetcher:
    """
    Class responsible for interacting with the Poke API to fetch berry data.
    """
    def __init__(self):
        self.api_url = getenv("BERRY_API", "https://pokeapi.co/api/v2/berry")
        self.all_data = self.get_paginated_data()

    def fetch_data(self, url: str):
        """ Fetch data from api """
        try:
            response = requests.get(url, timeout=API_TIMEOUT)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestsDependencyWarning as e:
            print(f"Error fetching data: {e}")
            data = {}

        return data


    def get_paginated_data(self) -> list:
        """ Create all necesary data """
        all_data = []

        while self.api_url:
            page_data = self.fetch_data(self.api_url)
            all_data.extend(page_data['results'])
            self.api_url = page_data.get('next')
        return all_data
