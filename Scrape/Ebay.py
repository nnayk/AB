# import from modules  within project
from Scrape.Scraper import onlineScraper
from Scrape.Utillities import Utilities
# import scraping packages
from bs4 import BeautifulSoup
import requests


class Ebay(onlineScraper):
    def __init__(self, product, htmlTitle, htmlLink, htmlPrice,htmlCondition,htmlShipping) -> None:
        self.product = product
        # html_title is a 2-element dictionary with index 0 = html tag for product title and index 1 = html class for product title
        self.htmlTitle = htmlTitle
        # html_link is a 2-element dictionary with index 0 = html tag for product link and index 1 = html class for product link
        self.htmlLink = htmlLink
        self.htmlPrice = htmlPrice
        self.htmlCondition = htmlCondition
        self.htmlShipping = htmlShipping

        self.page = requests.get(
            f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={product}&_sacat=0")
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def specialShipping(self):
        pass

    # ebay specific methods -- no overriding methods
    # def
