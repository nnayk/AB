# import from modules  within project
from Scrape.Scraper import onlineScraper
from Scrape.Utillities import Utilities
# import scraping packages
from bs4 import BeautifulSoup
import requests


class Ebay(onlineScraper):
    def __init__(self, store,product, htmlTitle, htmlLink, htmlPrice,htmlCondition,htmlShipping) -> None:
        self.store = store
        self.product = product
        # html_title is a 2-element dictionary with index 0 = html tag for product title and index 1 = html class for product title
        self.htmlTitle = htmlTitle
        # html_link is a 2-element dictionary with index 0 = html tag for product link and index 1 = html class for product link
        self.htmlLink = htmlLink
        self.htmlPrice = htmlPrice
        self.htmlCondition = htmlCondition
        self.htmlShipping = htmlShipping

        self.listings = requests.get(
            f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={product}&_sacat=0")
        self.generalSoup = BeautifulSoup(self.listings.content, "html.parser")


    def getSellerInfo(self,prodLinks,sortType):
        '''gets each product's seller info,description,etc.'''
        sellerRatings=[]
        sellerFeedback=[]
        for link in prodLinks:
            itemId=str(link[link.index("itm")+1:link.index("?")])
            itemPage = requests.get(f"https://www.ebay.com/itm/{itemId}")
            itemSoup = BeautifulSoup(itemPage.content, "html.parser")
            sellerFeed = (itemSoup.find("span",class_="mbg-l").text)[:-1].strip()
            #print(f"billy={sellerRating}")
            #print(f"billy={(int)(sellerRating[sellerRating.index('(')+1:sellerRating.index(')')-1])}")
            if sortType=="feedback":
                try:
                    print(f"selly111={sellerFeed}")
                    sellerFeed = (int)(sellerFeed[sellerFeed.index('(')+1:])
                except: 
                    print(f'sel22222={sellerFeed}')
                sellerFeedback.append(sellerFeed)

            elif sortType=="reviews":
                sellerRate= itemSoup.find("div",id="si-fb").text
                try:
                    sellerRate = (float)(sellerRate[0:sellerRate.index('%')])
                except:
                    print(f"sellerRating={sellerRate}")
                print(f"fallu={sellerRate}")
                sellerRatings.append(sellerRate)
            
        if sortType=="feedback":
            return sellerFeedback
        print("jagga")
        return sellerRatings
        #print(f"sellerRating={sellerRatings},sellerFeedback={sellerFeedback}")
    def specialShipping(self):
        pass

    # ebay specific methods -- no overriding methods
    # def
