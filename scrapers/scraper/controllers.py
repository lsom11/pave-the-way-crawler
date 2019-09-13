from flask import Blueprint

from scrapers.factory.factory import Creator

scraper_blueprint = Blueprint('slack', __name__)


@scraper_blueprint.route('/', methods=['POST'])
def scrape():
    site = request.form.get('site')
    scraper = Creator(site)

    return scraper, 200
