class ShoppingCart :
    def __init__(self)-> None:
        self.__total_price = 0
        self.__list_product_cart = []
        self.__amount = 0

    def add_product_to_shopping_cart(self, selected_product) :
        self.__list_product_cart.append(selected_product)
        self.__amount += selected_product.amount
        self.calculate_total_price(selected_product)
        if selected_product in self.__list_product_cart:
            return {"data": "added successfully"}
        else: 
            {"data": "Failed to add"}

    def delete_product_from_shopping_cart(self, product, color_id, size) :
        for selected_product in self.__list_product_cart:
            if selected_product.id == product.product_id:
                if selected_product.color_id == color_id:
                    if selected_product.size == size:      
                        self.__list_product_cart.remove(selected_product)
                        self.__total_price -= selected_product.price
                        self.__amount -= selected_product.amount
                        return {"data": "deleted  successfully"}
        return {"data": "Not found"}
    
    def updete_amount(self, product, amount, price):
        for selected_product in self.__list_product_cart:
            if selected_product.id == product.id :
                if selected_product.color_id == product.color_id:
                    if selected_product.size == product.size:
                        self.__amount += amount
                        self.__total_price += amount*price
                        return {"data": "added successfully"}
        return {"data": "Failed to add"}

    def calculate_total_price(self, selected_product) :
        self.__total_price += selected_product.price

    @property
    def total_price(self):
        return self.__total_price
    @property
    def list_product_cart(self):
        return self.__list_product_cart
