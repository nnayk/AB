#main file to run that takes care of input and communicates with other files

#import from modules  within project
from Scrape.Ebay import Ebay
from Scrape.Utillities import Utilities
#import scraping packages
from bs4 import BeautifulSoup
import requests

class General:
    def __init__(self,store) -> None:
        self.store = store.capitalize()

    def startScrape(self,productIn,sort_by):
        if self.store=="Ebay":
            link=f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={productIn}&_sacat=0"
            utils = Utilities()

            ebayObj = Ebay(productIn,utils.initDicts("h3","s-item__title"),utils.initDicts(htmlClass="s-item__link"),utils.initDicts("span","s-item__price"),utils.initDicts("span","SECONDARY_INFO"),utils.initDicts("span","s-item__shipping s-item__logisticsCost"))

            productLs,remove = ebayObj.getNames() #contains indexes of products from pdouct_ls that do not have proper/complete information
            #print(f"remove{remove}")
            productLinks = ebayObj.getLinks()
            utils.delProducts(remove,productLinks)
            productConditions = ebayObj.getConditions()
            productPrice = ebayObj.getPrices()
            productShip = ebayObj.getShipping()
            productImages = ebayObj.getImages()
            #print(f"productship={productShip},lengthy={len(productShip)}")
            #print(f"absaj={len(productLs)}")
            #print(f"ls={len(productLs)}\nlinks={len(productLinks)}\nprices={len(productPrice)}")

            #for i,product in enumerate(productLs):
                        #print(f"{i} Product Name: {product}")

            productList = utils.orgProdInfo(productLs,productPrice,productLinks,productConditions,productShip,productImages)
            if sort_by=="price":
                productList = ebayObj.sortByPrice(productList)
            return productList
           # ebayObj.prodInfo = utils.orgProdInfo(productLs,productPrice,productLinks)

            #for key,value in ebayObj.prodInfo.items():
             #   print(f"{key}:{value}")

#gen=General("Ebay")
#gen.startScrape("shoe")



