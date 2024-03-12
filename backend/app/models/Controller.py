from .Product import Product
from .User import Customer
class Controller:
    def __init__(self)-> None:
        self.__list_order = []
        self.__list_product = []
        self.__list_category = ["Men", "Women", "Kids"]
        self.__list_customer = []
        self.__list_admin = []

    def get_all_product(self):
        return self.__list_product

    def add_to_product_list(self, product):
       if product not in self.__list_product:
            self.__list_product.append(product)
            return self.__list_product
    
    def add_to_order_list(self, order):
       if order not in self.__list_order:
            self.__list_order.append(order)
            return self.__list_order
       
    def add_to_admin_list(self, admin):
        if admin not in self.__list_admin:
            self.__list_admin.append(admin)
            return self.__list_admin
        
    def add_to_customer_list(self, customer):
        if customer not in self.__list_customer:
            self.__list_customer.append(customer)
            return self.__list_customer

    def search_product_by_id(self, product_id):
        for product in self.__list_product :
            if product_id == product.product_id:
                return product   
        return {"Data ": "Not found "} 
    
    def search_product_by_name_for_customer(self, keyword):
        matching_products = []
        for product in self.__list_product:
            if keyword.lower() in product.product_name.lower():
                matching_products.append(product)
        if matching_products:
            return matching_products
        else:
            return {"Data": "Not found"}
        
    def search_product_by_name(self, name):
        for product in self.__list_product :
            if name == product.product_name:
                return product   
        return {"Data ": "Not found "} 
     
    def search_product_in_category(self, category):
        list_product_category  = []
        for product in self.__list_product: 
            if category == product.category:
                list_product_category.append(product)
        return list_product_category
    
    def search_customer_by_id (self, customer_id):
        for customer in self.__list_customer :
            if customer_id == customer.account.id:
                return customer
        return {"Data ": "You haven't already register"}
    
    def search_admin_by_id(self, admin_id):
        for admin in self.__list_admin:
            if admin.admin_id == admin_id :
                return admin
        return {"Data ": "You haven't already Login"} 
    
    def register(self, name, email, password):
        for admin in self.__list_admin :
            if admin.email == email :
                return {"data" : "You already have an account"}
        for customer in self.__list_customer:
            if customer.account.email == email :
                return {"data" : "You already have an account."}
        self.add_to_customer_list(Customer(name, email, password))
        return {"data": "successfully"}
    
    def login(self, email, password):
        for customer in self.__list_customer:
            if customer.account.email == email:
                if customer.account.password == password:
                    return customer.account.id
        return{"data": "Please check your email or password and try again!"}
    
    def add_to_cart(self, customer_id, product_id, color_id, size, amount):
        customer = self.search_customer_by_id(customer_id) 
        if customer != {"Data ": "You haven't already register"}  :
            product = self.search_product_by_id(product_id)
            result = customer.add_to_cart(product, color_id, size, amount)
            return result
        return customer
    
    def delete_from_cart(self, customer_id, product_id, color_id, size):
        customer = self.search_customer_by_id(customer_id)
        product = self.search_product_by_id(product_id)
        result = customer.delete_from_cart(product, color_id, size)
        return result
    
    def shopping_cart(self, customer_id):
        customer = self.search_customer_by_id(customer_id) 
        if customer != {"Data ": "You haven't already register"}  :
            result = customer.shopping_cart
            return result
        return customer
    
    def toggle_favorite(self, customer_id, product_id):
        customer = self.search_customer_by_id(customer_id) 
        if customer != {"Data ": "You haven't already register"}  :
            product = self.search_product_by_id(product_id)
            result = customer.toggle_favorite(product)
            return result
        return customer
        
    def view_favorite(self, customer_id):
        customer = self.search_customer_by_id(customer_id) 
        if customer != {"Data ": "You haven't already register"}  :
            result = customer.list_favorite
            return result
        return customer
    
    def add_address(self, customer_id, house_number, soi, road, province, postal_code):
        customer = self.search_customer_by_id(customer_id) 
        if customer != {"Data ": "You haven't already register"} :
            result = customer.add_address(house_number, soi, road, province, postal_code)
            return result
        return customer
    
    def delete_address(self, customer_id, address_id):
        customer = self.search_customer_by_id(customer_id) 
        if customer != {"Data ": "You haven't already register"} :
            result = customer.delete_address(address_id)
            return result
        return customer

    def view_address(self, customer_id):
        customer = self.search_customer_by_id(customer_id) 
        if customer != {"Data ": "You haven't already register"}  :
            result = customer.list_address
            return result
        return customer
    
    def choose_address(self, customer_id, address_id):
        customer = self.search_customer_by_id(customer_id) 
        result = customer.choose_address(address_id)
        return result
    
    def add_credit_card(self, customer_id, type_card, card_name, number, pin_number):
        customer = self.search_customer_by_id(customer_id) 
        if customer != {"Data ": "You haven't already register"} :
            result = customer.add_credit_card(type_card, card_name, number, pin_number)
            return result
        return customer
    
    def delete_credit_card(self, customer_id, number):
        customer = self.search_customer_by_id(customer_id) 
        if customer != {"Data ": "You haven't already register"} :
            result = customer.delete_credit_card(number)
            return result
        return customer
    
    def view_credit_card(self, customer_id):
        customer = self.search_customer_by_id(customer_id) 
        if customer != {"Data ": "You haven't already register"}  :
            result = customer.list_credit_card
            return result
        return customer
     
    def choose_credit(self, customer_id, credit_id):
        customer = self.search_customer_by_id(customer_id) 
        result = customer.choose_credit(credit_id)
        return result
    
    def update_phone(self, customer_id, phone):
        customer = self.search_customer_by_id(customer_id) 
        if customer != {"Data ": "You haven't already register"} :
            customer.phone = phone
            return {"Data ": "Updated"}
        return customer 
    
    def buy_product(self, customer_id):
        customer = self.search_customer_by_id(customer_id) 
        if customer != {"Data ": "You haven't already register"} :
            result = customer.buy_product()
            return result
        return customer
    
    def create_order(self, customer_id, address_id):
        customer = self.search_customer_by_id(customer_id) 
        result = customer.create_order(address_id, customer_id)
        self.__list_order.append(result[1])
        return result[0]
    
    def view_order(self, customer_id):
        customer = self.search_customer_by_id(customer_id) 
        result = customer.list_order
        return result
    
    def pay_money(self, customer_id, number, order_id):
        customer = self.search_customer_by_id(customer_id) 
        result = customer.pay_money(number, order_id)
        if result == {"data": "successfull"}:
            for selected_product in customer.shopping_cart.list_product_cart:
                product_id = selected_product.id
                color_id = selected_product.color_id
                size = selected_product.size
                amount = selected_product.amount
                product = self.search_product_by_id(product_id)
                for product_style in product.list_product_style:
                    if product_style.product_style_id == color_id:
                        if product_style.size == size:
                            product_style.stock.amount_stock -= amount
            customer.clear_shopping_cart() 
            return {"data": "Done"}
        return result
    
    def update_order(self, order_id, admin_id, status):
        for order in self.__list_order:
            if order.order_id == order_id:
                admin = self.search_admin_by_id(admin_id)
                result = admin.updete_status(order, status)
                customer = self.search_customer_by_id(order.customer_id)
                customer.update_history()
                return result
        return  {"Data ": "Not found"}
    
    def view_profile(self, customer_id):
        customer = self.search_customer_by_id(customer_id) 
        if customer != {"Data ": "You haven't already register"}  :
            result = customer.view_profile()
            return customer.name,customer.email, customer.phone, result
        return customer   
    
    def view_account_detail(self, customer_id):
        customer = self.search_customer_by_id(customer_id) 
        if customer != {"Data ": "You haven't already register"}  :
            result = customer.view_account_detail()
            return customer.name, customer.email, customer.phone, result
        return customer  
    
    def add_product(self, product_name, price, category, product_style  ):
        if self.search_product_by_name(product_name) == {"Data ": "Not found "} :
            self.add_to_product_list(Product(product_name, price, category, product_style))
            return {"data": "added successfully"}
        return {"data": "added not successfully"}
    
    def delete_product(self, product_id):
        for product in self.__list_product:
            if product.product_id == product_id :
                self.__list_product.remove(product)
                return {"data": "deleted successfully"}
        return {"data": "Not found"}

    @property
    def check_order(self):
        return self.__list_order
    @property
    def list_product(self):
        return self.__list_product
    @property
    def list_category(self):
        return self.__list_category
    @property
    def list_customer(self):
        return self.__list_customer
