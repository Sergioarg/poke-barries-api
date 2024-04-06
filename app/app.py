""" Main API of Berries Stats"""
from os import getenv, path
from flask import Flask, jsonify, render_template, Blueprint
from flask_caching import Cache

from .berries.berry_data_fetcher import BerryDataFetcher
from .berries.berry_statistics import BerryStatistics
from .berries.histogram_generator import HistogramGenerator

# Confurations constans
API_HOST = getenv("API_HOST", "127.0.0.1")
API_PORT = getenv("API_PORT", "5000")

# Initilization of flask and blueprints
app = Flask(__name__, static_folder='static')
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
berries_bp = Blueprint(name='allBerryStats', import_name=__name__)

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


@berries_bp.route('/', methods=['GET'])
@cache.cached(timeout=50)
def get_all_berries_stats():
    """ Return barries stats """
    berry_statistics = BerryStatistics(BerryDataFetcher())
    response = berry_statistics.get_stats()
    return jsonify(response)


@berries_bp.route('/histogram')
def histogram_view():
    """ Render the histogram page """
    histogram_path = 'app/static/imgs/histogram.png'

    if not path.exists(histogram_path):
        berry_statistics = BerryStatistics(BerryDataFetcher())
        histogram_generator = HistogramGenerator(berry_statistics)
        histogram_generator.generate_histogram()

    template = 'histogram.html'
    return render_template(template)

# Register Blueprint in app
app.register_blueprint(berries_bp, url_prefix='/api/v1/allBerryStats')

if __name__ == '__main__':
    app.run(host=API_HOST, port=API_PORT) # type: ignore
