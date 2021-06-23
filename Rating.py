# from Customer import *
# from Product import *

class Rating:
    def __init__(self, id, productId, customerId,stars,review):
        self.id = id
        self.productId = productId
        self.customerId = customerId
        self.stars = stars
        self.review = review


    def starsOverall(self):
        while True:
            try:
                userInput = int(input("Enter a star rating between 0 and 5"))
                if userInput >= 0 and userInput <= 5:
                    print("Thank You")
                    break
            except ValueError:
                print("Invalid star rating! Try again.")
                continue
            return self.stars

    def rewiewText(self):
        text = input("Your review")
        return self.review

    def __str__(self):
        return f"{self.id} {self.productId} {self.customerId} Rating - {self.stars} Rewiew: {self.review}"

    def __repr__(self):
        return self.__str__()

