""" Main API of Berries Stats"""
from os import getenv
from flask import Flask, jsonify, render_template
from flask_caching import Cache

from .berries.berry_data_fetcher import BerryDataFetcher # pylint: disable=E0611, E0401
from .berries.berry_statistics import BerryStatistics
from .berries.histogram_generator import HistogramGenerator


app = Flask(__name__, static_folder='static')
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

API_HOST = getenv("API_HOST", "127.0.0.1")
API_PORT = getenv("API_PORT", "5000")
CACHE_TIME_OUT = 50

@app.route('/', methods=['GET'])
def base_endpoint():
    """ Base endpoint to get information about the API """
    response = {
        "message": "Poke-berries statistics API",
        "version": "1.0",
        "endpoints": {
            "berries": f"{API_HOST}:{API_PORT}/api/v1/berries/",
            "histogram": f"{API_HOST}:{API_PORT}/api/v1/berries/histogram"
        }
    }
    return jsonify(response)


@app.route('/api/v1/berries/', methods=['GET'])
@cache.cached(timeout=CACHE_TIME_OUT)
def get_all_berries_stats():
    """ Return barries stats """

    berry_data_fetcher = BerryDataFetcher()
    berry_statistics = BerryStatistics(berry_data_fetcher)
    histogram_generator = HistogramGenerator(berry_statistics)
    histogram_generator.generate_histogram()
    response = berry_statistics.get_stats()

    return jsonify(response)


@app.route('/api/v1/berries/histogram')
def histogram_view():
    """ Render the histogram page """
    template = 'histogram.html'
    return render_template(template)


if __name__ == '__main__':
    app.run(host=API_HOST, port=API_PORT)
