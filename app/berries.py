""" Module about manage data of Berry from Poke API """
from os import getenv, path, makedirs
import matplotlib.pyplot as plt
import requests
from dotenv import load_dotenv
from app.operations import MathOperations


load_dotenv()
class Berries:
    """ Interactions with PokeAPI """
    def __init__(self, math_ops: MathOperations):
        self.api_url = getenv("BERRY_API", "https://pokeapi.co/api/v2/berry")
        self.math_ops = math_ops
        self.all_data = self.get_paginated_data()
        self.berries_names = self.get_berries_names()
        self.growth_times = self.get_berry_growth_times()
        self.min_growth_time = min(self.growth_times)
        self.max_growth_time = max(self.growth_times)

    def fetch_data(self, url: str):
        """ Fetch data from api """

        response = requests.get(url, timeout=30)

        if response.status_code == 200:
            response.raise_for_status()
            data = response.json()
        else:
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

    def get_berries_names(self) -> list:
        """ Create a list with names of berries """
        names = [item['name'] for item in self.all_data]
        names.sort()
        return names

    def get_berry_growth_times(self) -> list:
        """ Create a list with valoues of growth """
        growth_times = []

        for berry in self.all_data:
            berry_data = self.fetch_data(berry['url'])
            growth_time = berry_data['growth_time']
            growth_times.append(growth_time)

        return growth_times

    def get_barries_stats(self) -> dict:
        """ Return the stats of the berries """
        growth_times = self.growth_times
        min_growth_time = self.min_growth_time
        median_growth_time = self.math_ops.calculate_median(growth_times)
        max_growth_time = self.max_growth_time
        variance_growth_time = self.math_ops.calculate_variance(growth_times)
        mean_growth_time = self.math_ops.calculate_mean(growth_times)
        frequency_growth_time = self.math_ops.calculate_frequency_growth_times(
            growth_times)
        self.generate_histogram()
        return {
            "berries_names": self.berries_names,
            "min_growth_time": min_growth_time,
            "median_growth_time": median_growth_time,
            "max_growth_time": max_growth_time,
            "variance_growth_time": variance_growth_time,
            "mean_growth_time": mean_growth_time,
            "frequency_growth_time": frequency_growth_time
        }

    def generate_histogram(self):
        """ Generate the image of histogram data file """
        plt.hist(
            self.growth_times,
            bins=range(self.min_growth_time, self.max_growth_time + 1),
            edgecolor='black'
        )

        plt.title('Histogram of Berry Growth Times')
        plt.xlabel('Growth Time')
        plt.ylabel('Frequency')

        imgs_path = 'app/static/imgs'

        if not path.exists(imgs_path):
            makedirs(imgs_path)

        plt.savefig(f'{imgs_path}/histogram.png')
        plt.close()
