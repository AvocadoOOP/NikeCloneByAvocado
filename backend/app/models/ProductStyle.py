from .Stock import Stock
class ProductStyle:
    __product_style_id = 0
    def __init__(self, color, stock, size):
        ProductStyle.__product_style_id += 1
        self.__product_style_id = ProductStyle.__product_style_id
        self.__color = color
        self.__size = size
        self.__stock = Stock(size, stock)

    @property
    def product_style_id(self):
        return self.__product_style_id
    @property
    def color(self):
        return self.__color
    @property
    def size(self):
        return self.__size
    @property
    def stock(self):
        return self.__stock