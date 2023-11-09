def addToCart(userIds, name, productName, prodQuantity, addTOCart, groceries):
    
    try:
        if name not in userIds:
            raise Exception("User not found, please register with us")
        else:
            if productName not in groceries.keys():
                raise Exception("Product not present in our inventory")
            else:
                for item in list(groceries.keys()):
                    if productName == item:
                        if prodQuantity > groceries[productName]:
                            raise Exception("Product Quantity is out of stock")
                        else:
                            addTOCart.append(productName)
                            return({
                                "message":f"{productName} of {prodQuantity} is added by user {name}",
                                "data":addTOCart
                            })

    except Exception as ex:
        return({
            "message":str(ex),
            "data":None
        })

db = {
    1:"raja",
    2:"Sandhya",
    3:"Vamshi",
    4:"bhargava",
    5:"gopi",
    6:"pusgpavati"
}

addTOCart = []
groceries = {"apples":10, "bananas":15, "carrots":20, "eggs":100, "milk":20, "bread":30, "chicken": 50, "rice": 200, "pasta":20, "onions":30}

userNamesList = list(dict.values(db))
currentCustomerUserName = "gopi"
productName = "rice"
prodQuantity = 50
res = addToCart(userNamesList, currentCustomerUserName, productName, prodQuantity, addTOCart, groceries)
print(res)