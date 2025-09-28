import re
from datetime import datetime
def valid_email(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

class ShoppingSystem:
    def __init__(self):
        self.customer = {}
        self.products = {}
        self.order = []
    def register_customer(self,customer):
        self.customer[customer.id] = customer
    def add_product(self,product):
        self.products[product.id] = product
    def view_products(self):
        for i in self.products.keys():
            print(self.products[i])
    def process_order(self, customer: "Customer", order: "Order", payment_method): 
        customer.cart.clear_cart()
        customer.orders[order.id] = order
        order.process_payment(payment_method)
        print("Processed successfully!")

class Customer:
    id = 0
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.id = Customer.id
        Customer.id += 1
        self.cart = Shopping_cart()
        self.orders = {}
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,email):
        if not valid_email(email):
            raise ValueError('wrong email')
        self.__email = email
    def add_product(self,product):
        self.cart.add_product(product)
    def remove_from_cart(self,product):
        self.cart.remove_product(product)
    def view_cart(self):
        self.cart.view_cart()
    def place_order(self,payment_method):
        order = Order()
        for i in self.cart.products.keys():
            order.add_products(self.cart.products[i])
        return order
    def view_orders(self):
        if not self.orders:
            print("There is no such element")
        else:
            for key in self.orders.keys():
                self.orders[key].view_order_details()

class Shopping_cart:
    id = 0
    def __init__(self):
        self.id = Shopping_cart.id
        Shopping_cart.id += 1
        self.products = {}
    def add_product(self,product):
        print(product.id)
        self.products[product.id] = product
    def remove_product(self,product):
        if not self.products:
            print('cart is empty')
            return
        for i in self.products.keys():
            if self.products[i] == product:
                self.products.pop(i)
                break
        else:
            print('no such product to remove')
    def view_cart(self):
        for i in self.products.keys():
            self.products[i].view_product_details()
    def clear_cart(self):
        self.products = {}

class Product:
    id = 0
    def __init__(self,name,price,description,availability):
        self.name = name
        self.price = price
        self.description = description
        self.availability = availability
        self.id = Product.id
        Product.id += 1
    def view_product_details(self):
        print(self.name,self.price,self.availability,self.description)
    def check_availability(self):
        if self.availability:
            print('product is available')
        else:
            print('product is not available')
class Order:
    id = 0
    def __init__(self):
        self.status = 'waiting'
        self.id = Order.id
        Order.id += 1
        self.products = []
    def add_products(self,product):
        self.products.append(product)
    def remove_product(self,product):
        self.products.remove(product)
    def update_status(self,status):
        self.status = status
    def process_payment(self,payment_method):
        sum = 0
        for i in self.products:
            sum += i.price
        payment = Payment(sum,payment_method)
        self.payment = payment
    def view_order_details(self):
        print(self)
    
    def __str__(self):
        return f"Order\nProducts: {self.products}\nStatus: {self.status}\nPayment: {self.payment}"

class Payment:
    payment_id = 0
    def __init__(self, amount, payment_method):
        self.id = Payment.payment_id
        Payment.payment_id += 1
        self.amount = amount
        self.payment_method = payment_method
        self.payment_date = datetime.now()
        
    def view_payment_details(self):
        print(self)
        
    def __str__(self):
        return f"Payment: \nAmount: {self.amount}\nPayment method: {self.payment_method}\nPayment Date: {self.payment_date}"

        
c1 = Customer("Sasha", "abcd@shnik.ru")

sh = ShoppingSystem()
sh.register_customer(c1)
p1 = Product("Case", 1000.0, "Shat lav case e", True)
p2 = Product("Shor", 1000.0, "Shat lav case e", True)
p3 = Product("Koshik", 1000.0, "Shat lav case e", True)

sh.add_product(p1)
sh.add_product(p2)
sh.add_product(p3)

c1.add_product(p1)
c1.add_product(p2)
c1.add_product(p3)
c1.view_cart()

o1 = c1.place_order("kanxik")
sh.process_order(c1, o1, "kanxik")