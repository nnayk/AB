class Utilities:
    #functions for general use
    #in accordance with DRY, this function is used often and returns a dictionary with html tag and class info
    def initDicts(self,htmlTag=None,htmlClass=None):
        return {"tag":str(htmlTag),"class":str(htmlClass)}

    #organizes product info into a concise dictionary where product name maps to its attributes
    def orgProdInfo(self,prodNames,prodPrices,prodLinks,prodConds,prodShip,prodImages):
        #format: {}
        productCompleteList = []
        #code repetition unfortunately appears to be inevitable here since the existence of 
        #each piece of scraped information must be individually checked 
        for i in range(len(prodNames)):
            prodDict={}
            try:
                prodDict['name'] = prodNames[i]
            except:
                prodDict['name'] = "Check Link"

            try:
                prodDict['price'] = prodPrices[i]
            except:
                prodDict['price'] = "Check Link"
            
            try:
                prodDict['link'] = prodLinks[i]
            except:
                prodDict['link'] = "Check Link"
            
            try:
                prodDict['condition'] = prodConds[i]
            except:
                prodDict['condition'] = "Check Link"
            
            try:
                prodDict['shipping'] = prodShip[i]
            except:
                prodDict['shipping'] = "Check Link"
            
            try:
                prodDict['image'] = prodImages[i]
            except:
                prodDict['image'] = "Check Link"

            productCompleteList.append(prodDict.copy())
        print("HELLO WORLD")
        print(f"jsahdkas={productCompleteList}")
        return productCompleteList



    #removes faulty products (i.e. do not have complete information)
    def delProducts(self,remove,prodLinks):
        for index in remove:
            prodLinks.pop(index)

