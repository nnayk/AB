#main file to run that takes care of input and communicates with other files

#import from modules  within project
from Ebay import Ebay
from Utillities import Utilities
#import scraping packages
from bs4 import BeautifulSoup
import requests

class GUI:
    def __init__(self,store) -> None:
        self.store = store.capitalize()


        
productIn = input("Product: ")
link=f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={productIn}&_sacat=0"

guiObj = GUI("Ebay")
utils = Utilities()

ebayObj = Ebay(productIn,utils.initDicts("h3","s-item__title"),utils.initDicts(htmlClass="s-item__link"),utils.initDicts("span","s-item__price"))

productLs,remove = ebayObj.getNames() #contains indexes of products from pdouct_ls that do not have proper/complete information
#print(f"remove{remove}")
productLinks = ebayObj.getLinks()
utils.delProducts(remove,productLinks)
productPrice = ebayObj.getPrices()
#print(f"ls={len(productLs)}\nlinks={len(productLinks)}\nprices={len(productPrice)}")

#for i,product in enumerate(productLs):
            #print(f"{i} Product Name: {product}")

ebayObj.prodInfo = utils.orgProdInfo(productLs,productPrice,productLinks)

for key,value in ebayObj.prodInfo.items():
    print(f"{key}:{value}")



