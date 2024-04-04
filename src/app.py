""" Main API of Berries Stats"""
from os import getenv
from flask import Flask, jsonify
from flask_caching import Cache
from berries import Berries
from operations import MathOperations


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/', methods=['GET'])
def base_endpoint():
    """ Base endpoint """
    response = {
        "message": "Poke-berries statistics API",
        "version": "1.0",
        "endpoints": {
            "base": "/",
            "berries": "/api/v1/berries/stats"
        }
    }
    return jsonify(response)


@app.route('/api/v1/berries/stats', methods=['GET'])
@cache.cached(timeout=50)
def get_all_berries_stats():
    """ Return barries stats """
    math_ops = MathOperations()
    berries = Berries(math_ops)

    response = berries.get_barries_stats()
    return jsonify(response)


if __name__ == '__main__':

    api_host = getenv("API_HOST", "127.0.0.1")
    api_port = getenv("API_PORT", "5000")

    app.run(host=api_host, port=api_port, debug=True)
