class Product:
    def __init__(self, name, price, stock , category , description):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.description = description

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_stock(self, stock):
        self.stock = stock

    def get_des(self , description):
        self.description = description 
    
    def get_cat(self , category):
        self.category = category 






