from .ProductStyle import ProductStyle
class Product:
    __product_id = 0
    def __init__(self, product_name, price, category, total_product_style,list_images):
        Product.__product_id += 1
        self.__product_id = Product.__product_id
        self.__product_name = product_name
        self.__price = price
        self.__category = category
        self.__list_product_style = []
        self.__list_images = list_images
        self.add_list_product_style(total_product_style)

    def add_list_product_style(self, total_product_style):
        print(total_product_style)
        for key, val in total_product_style.items() :
            product_style = ProductStyle(key, val[0] , val[1])
            self.__list_product_style.append(product_style)


    @property
    def price(self):
        return self.__price
    @property
    def product_id(self):
        return self.__product_id
    @property
    def product_name(self):
        return self.__product_name
    @property
    def category(self):
        return self.__category
    @property
    def list_product_style(self):
        return self.__list_product_style
    
    @property
    def list_images(self):
        return self.__list_images
