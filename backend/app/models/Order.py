from .Payment import Payment
from .Delivery import Delivery
import datetime
class Order:
    __order_id = 0
    def __init__(self, address, shopping_cart, customer_id):
        Order.__order_id += 1
        self.__order_id = Order.__order_id
        self.__customer_id = customer_id
        self.__address =  address
        self.__shopping_cart = shopping_cart
        self.__payment = Payment()
        self.__delivery = Delivery()
        self.__payment_status = None
        self.__delivery_status = None
        self.__date = datetime.datetime.now()

    def pay_money(self, credit_card):
        price = self.__shopping_cart.total_price
        result = self.__payment.pay_money(credit_card, price)
        self.__payment_status = self.__payment.payment_status
        return result
    
    def updete_status(self, status):
        result = self.__delivery.updete_status(status)
        self.__delivery_status = self.__delivery.delivery_status
        return result

    @property
    def order_id(self):
        return self.__order_id
    @property 
    def address(self):
        return self.__address 
    @property 
    def shopping_cart(self):
        return self.__shopping_cart 
    @property
    def payment_status(self):
        return self.__payment_status
    @property
    def delivery_status(self):
        return self.__delivery_status
    @property
    def customer_id(self):
        return self.__customer_id