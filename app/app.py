""" Main API of Berries Stats"""
from os import getenv
from flask import Flask, jsonify, render_template
from flask_caching import Cache
from app.berries import Berries
from app.operations import MathOperations as math_ops


app = Flask(__name__, static_folder='static')
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

API_HOST = getenv("API_HOST", "127.0.0.1")
API_PORT = getenv("API_PORT", "5000")

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
@cache.cached(timeout=50)
def get_all_berries_stats():
    """ Return barries stats """
    berries = Berries(math_ops())
    response = berries.get_barries_stats()
    return jsonify(response)


@app.route('/api/v1/berries/histogram')
def histogram_view():
    """ Render the histogram page """
    template = 'histogram.html'
    return render_template(template)


if __name__ == '__main__':
    app.run(host=API_HOST, port=API_PORT)
