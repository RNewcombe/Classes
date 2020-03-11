class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def myfunc(self):
      print("The price is " + self.price)

    
p1 = Stock("Brennans breads",2)
p1.myfunc()
