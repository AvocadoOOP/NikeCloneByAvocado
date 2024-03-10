class Stock :
    def __init__(self, size, amount_stock):
        self.__size = size
        self.__amount_stock = amount_stock

    @property
    def product_style_id(self):
        return self.__product_style_id
    @property
    def color(self):
        return self.__color
    @property
    def amount_stock(self):
        return self.__amount_stock
    @amount_stock.setter
    def amount_stock(self, amount):
        self.__amount_stock = amount