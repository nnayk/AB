class Utilities:
    #functions for general use
    #in accordance with DRY, this function is used often and returns a dictionary with html tag and class info
    def initDicts(self,htmlTag=None,htmlClass=None):
        return {"tag":str(htmlTag),"class":str(htmlClass)}

    #organizes product info into a concise dictionary where product name maps to its attributes
    def orgProdInfo(self,prodNames,prodPrices,prodLinks):
        #format: {"Product Name": (Price,Link)}
        return {str(prodNames[i]):[prodPrices[i],prodLinks[i]] for i in range(len(prodNames))}


    #removes faulty products (i.e. do not have complete information)
    def delProducts(self,remove,prodLinks):
        for index in remove:
            prodLinks.pop(index)

