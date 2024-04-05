""" Module to manage the histogram """
# pylint: disable=too-few-public-methods
from os import path, makedirs
import matplotlib.pyplot as plt
from .berry_statistics import BerryStatistics

class HistogramGenerator:
    """
    Class responsible for interacting with the Poke API to fetch berry data.
    """
    def __init__(self, berry_statistics: BerryStatistics):
        self.berry_statistics = berry_statistics

    def generate_histogram(self):
        """ Generates and saves the histogram of the berry growth times. """
        plt.hist(
            self.berry_statistics.growth_times,
            bins=range(
                self.berry_statistics.min_growth_time,
                self.berry_statistics.max_growth_time + 1),
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
