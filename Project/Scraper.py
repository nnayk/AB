#Nakul Nayak
#OnlineScraper.py
#Description: GUI interface with backend web scraper that serves as an aid in finding good shopping deals on sites like Ebay, Amazon, etc.

#general scraper with methods applicable to all shopping platforms
class onlineScraper:
    def getNames(self):
        #print(soup.prettify())
        scrapedProducts = self.soup.find_all(str(self.htmlTitle["tag"]),class_=str(self.htmlTitle["class"]))
        cleanProducts=[]
        remove=[]
        for i,name in enumerate(scrapedProducts):
            if len(name)!=0:
                cleanProducts.append(name.text)
            else:
                remove.append(i)

        #z=soup.find_all("li",class_="s-item s-item__sep-on-bottom")
        #print(links)
        #x=officers.find_all("h3",class_="s-item__title")
        #for off in officers:
        #print(len(officers))
        #for i,product in enumerate(scrapedProducts):
        #    print(f"{i} Product Name: {product.text}")
        return cleanProducts,remove

    def getLinks(self):
        #print(f"self.htmlLink={self.htmlLink}")
        jumbledLinks = self.soup.find_all(class_=str(self.htmlLink["class"]))
        cleanLinks=[]
        for link in jumbledLinks:
            cleanLinks.append(link['href'])
        #for lin in cleanLinks:
            #print(lin)
    
        return cleanLinks

    def getPrices(self):
        scrapedPrices = self.soup.find_all(str(self.htmlPrice["tag"]),class_=str(self.htmlPrice["class"]))
        cleanPrices = []
        for price in scrapedPrices:
            cleanPrices.append(price.text)
        #print(f"Clean prices={cleanPrices}")
        #for pr in cleanPrices:
            #print(f"Price: {pr}")
        return cleanPrices
    
    def customPriceRange(self,min,max):
        validProducts = {}
        for product in self.prodInfo:
            price = self.prodInfo[product][0]
            if min<=price<=max:
                validProducts[product] = self.prodInfo[product]

        return validProducts
    
    def hasKeyword(self,word):
        validProducts = {}
        for product in self.prodInfo:
            if word in product:
                validProducts[product] = self.prodInfo[product]

        return validProducts

