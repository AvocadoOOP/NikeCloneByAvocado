from .ShoppingCart import ShoppingCart
from .Account import Account
from .SelectedProduct import SelectedProduct
from .Address import Address
from .CreditCard import CreditCard
from .Order import Order

class Person :
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    @property
    def name(self):
        return self.__name
    @property
    def email(self):
        return self.__email
    
class Customer(Person):
    def __init__(self, name, email, password):
        self.__phone = None
        self.__list_favorite = []
        self.__shopping_cart = ShoppingCart()
        self.__account = Account(email, password)
        self.__list_address = []
        self.__list_credit_card = []
        self.__list_order = []
        self.__order_history = []
        super().__init__(name, email)

    def toggle_favorite(self, product):
        if product not in self.__list_favorite:
            self.__list_favorite.append(product)
            return {"data": "added successfully"}
        else:
            self.__list_favorite.remove(product)
            return {"data": "deleted  successfully"}
        
    def add_to_cart(self, product, color_id, size, amount):
        product_id = product.product_id
        product_price = product.price
        for selected_product in  self.__shopping_cart.list_product_cart:
            if selected_product.id == product_id :
                if selected_product.color_id == color_id:
                    if selected_product.size == size:
                        selected_product.amount += amount
                        selected_product.calculate_price(product_price)
                        result = self.__shopping_cart.updete_amount(selected_product, amount, product_price)
                        return result          
        selected_product = SelectedProduct(product_id, product_price, color_id, size, amount)
        result = self.__shopping_cart.add_product_to_shopping_cart(selected_product)
        return result
    
    def delete_from_cart(self, product, color_id, size):
        result = self.__shopping_cart.delete_product_from_shopping_cart(product, color_id, size)
        return result
    
    def add_address(self, house_number, soi, road, province, postal_code):
        id_address = len(self.__list_address) + 1
        self.__list_address.append(Address(id_address, house_number, soi, road, province, postal_code))
        return {"data": "added successfully"}
    
    def delete_address(self, address_id):
        for address in self.__list_address:
            if address.id == address_id:
                self.__list_address.remove(address)
                return {"data": "deleted  successfully"}

    def add_credit_card(self, type_card, card_name, number, pin_number):
        self.__list_credit_card.append(CreditCard(type_card, card_name, number, pin_number))
        return {"data": "added successfully"}
    
    def delete_credit_card(self, number):
        for credit_card in self.__list_credit_card:
            if credit_card.number ==  number:
                self.__list_credit_card.remove(credit_card)
                return {"data": "deleted  successfully"}
        
    def buy_product(self):
        return self.__shopping_cart, self.__list_address
    
    def choose_address(self, address_id):
        for address in self.__list_address:
            if address.id == address_id:
                return address
        return {"data": "Not found"}

    def create_order(self, address_id, customer_id):
        for address in self.__list_address:
            if address.id == address_id:
                shopping_cart =  self.__shopping_cart
                order = Order(address, shopping_cart, customer_id)
                self.__list_order.append(order)
                return self.__list_credit_card, order
            
    def choose_credit(self, credit_id):
        for credit_card in self.__list_credit_card:
            if credit_card.id == credit_id:
                return {"Done"}
        return {"data": "Not found"}     
    
    def pay_money(self, number, order_id):
        for order in self.__list_order :
            if order.order_id == order_id:
                for credit_card in self.__list_credit_card:
                    if credit_card.number == number:
                        result = order.pay_money(credit_card)
                        return result
                    
    def clear_shopping_cart(self):
        self.__shopping_cart = ShoppingCart()
    
    def view_profile(self):
        return self.__list_order,self.__order_history 
    
    def update_history(self):
        for order in self.__list_order:
            if order.delivery_status  == "Order completed" :
                self.__list_order.remove(order)
                self.__order_history.append(order)

    def view_account_detail(self):
        return self.__list_address, self.__list_credit_card 

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone):
        self.__phone = phone
    @property
    def order_history(self):
        return self.__order_history 
    @property
    def list_order(self):
        return self.__list_order
    @property
    def list_credit_card(self):
        return self.__list_credit_card
    @property
    def list_favorite(self):
        return self.__list_favorite
    @property
    def list_address(self):
        return self.__list_address
    @property
    def shopping_cart(self):
        return self.__shopping_cart
    @property
    def account(self):
        return self.__account

class Admin(Person):
    __admin_id = 0
    def __init__(self, name, email, password):
        Admin.__admin_id += 1
        self.__admin_id = Admin.__admin_id
        self.__account = Account(email, password)
        super().__init__(name, email)

    def updete_status(self, order, status):
        result = order.updete_status(status)
        return result

    @property
    def admin_id(self):
        return self.__admin_id