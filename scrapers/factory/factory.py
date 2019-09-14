from scrapers.linkedin.scraper import LinkedInScraper
from scrapers.google.scraper import GoogleScraper
from scrapers.facebook.scraper import FacebookScraper

class ScraperCreator(site):
    def factory(type):
        if type == "LinkedIn":
            return LinkedInScraper()
        if type == "Google":
            return GoogleScraper()
        if type == "Facebook":
            return FacebookScraper()
        assert 0, "Bad shape creation: " + type
    factory = staticmethod(factory)
