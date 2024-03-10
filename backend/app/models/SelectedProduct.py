class SelectedProduct:
    def __init__(self, product_id, product_price, color_id, size, amount):
        self.__amount = amount
        self.__color_id = color_id
        self.__size = size
        self.__id = product_id
        self.__price = self.calculate_price(product_price)

    def calculate_price(self, product_price):
        self.__price = product_price * self.__amount
        return self.__price
    
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount):
        self.__amount = amount
    @property
    def color_id(self):
        return self.__color_id
    @property
    def size(self):
        return self.__size
    @property
    def price(self):
        return self.__price
    @property
    def id(self):
        return self.__id