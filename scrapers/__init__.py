from flask import Blueprint, jsonify, request

from scrapers.scraper.controllers import scraper_blueprint


from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

""" Corst settings will be here. We maybe use this endpoint later. """
cors = CORS(app, resources={
    r'/api/v1/*': {
        'origins': BaseConfig.ORIGINS
    }
})

app.register_blueprint(scraper_blueprint, url_prefix='/api/v1/scrape')

app.url_map.strict_slashes = False
