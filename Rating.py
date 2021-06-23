# from Customer import *
# from Product import *

class Rating:
    def __init__(self, id, productId, customerId,stars,review):
        self.id = id
        self.productId = productId
        self.customerId = customerId
        self.stars = stars
        self.review = review


    def __str__(self):
        return f"{self.id} {self.productId} {self.customerId} Rating - {self.stars} Rewiew: {self.review}"

    def __repr__(self):
        return self.__str__()

