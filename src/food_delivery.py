# Task
# we are required to create a food delivery system
# The task is complete the python code
# The user must be able to order food using the system with the following requirements:
# 1 Add food order details to the orders log
# 2 update the order pickup and delivery status
# 3 modify order items only if the order is not yet picked up
# 4 cancel the order if the order is not yet picked up
# 5 generate a total bill based on the provide details:
    # if(bill_amount > 1000): total_bill_amount = bill_amount + 10% tax
    # if(bill_amount < 1000): total_bill_amount = bill_amount + 5% tax

#FoodDeliverySystem:

class FoodDeliverySystem:
    order_id = 0
    orders_log = {}
    def __init__(self):
        self.menu = {
            "Burger": 150,
            "Pizza": 250,
            "Pasta": 200,
            "Salad": 120,
            "Beverages": 130,
            "Noodles": 150,
            "Sushi": 270,
            "Bakery":350
            # Add more items to the menu
        }
        self.bill_amount = 0

    def display_menu(self):
            """
            Return the menu details in the following format:
            Burger  |  150
            Pizza   |  250
            Pasta   |  200
            Salad   |  120
            Beverages  |  130
            Noodles  |  150
            Sushi   |  270
            Bakery  |  350
            """
            self.menu = {k: v for k, v in sorted(self.menu.items(), key=lambda item: item[1])}
            return "\n".join([f"{k}  |  {v}" for k, v in self.menu.items()])
        
        
    def place_order(self, customer_name, order_items):
        """
        Return orders log after order placed by a customer with status as "Placed", otherwise return "order placement failed"
        Format:
        orders_log = {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity"}, status = "Placed}}
        """
        self.order_id += 1
        self.orders_log[self.order_id] = {"customer_name": customer_name, "order_items": order_items, "status": "Placed"}
        return self.orders_log
        
    def pickup_order(self, order_id):
        """
        status: Picked Up	
        Return the changed status of the order: {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity"}, status = "Picked Up"}}
        """
        if order_id in self.orders_log:
            self.orders_log[order_id]["status"] = "Picked Up"
            return self.orders_log
        return "Order Not Found"
        
    def deliver_order(self, order_id):
        """
        status: Delivered
        Return the delivery status of order (delivered or not delivered)
        """
        
        if order_id in self.orders_log:
            self.orders_log[order_id]["status"] = "Delivered"
            return self.orders_log
        return "Order Not Found"
        
    def modify_order(self, order_id, new_items):
        """
        Return the modified order with items available in menu only if the order is not picked up:
        {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity", new_items}, status = "Placed"}}
        """
        if order_id in self.orders_log and self.orders_log[order_id]["status"] == "Placed":
            self.orders_log[order_id]["order_items"].update(new_items)
            return self.orders_log
        return "Order Not Found"
    
    def generate_bill(self, order_id):
        """
        if the sum of all items > 1000
        Amount = Sum of all items placed + 10% of total sum
        if sum of all items < 1000
        Amount = Sum of all items placed + 5% of total sum
        Return the total bill amount
        """
        if order_id in self.orders_log:
            self.bill_amount = sum([self.menu[item] * quantity for item, quantity in self.orders_log[order_id]["order_items"].items()])
            if self.bill_amount > 1000:
                return self.bill_amount + self.bill_amount * 0.1
            return self.bill_amount + self.bill_amount * 0.05
        return "Order Not Found"
        
    def cancel_order(self, order_id):
        """
        Cancel order items for the customer if the order is not Picked Up and remove order details from orders log
        Return the order logs. For example, if you have 3 orders, but the third order is cancelled, you need remove this from the orders log and just return the first two orders:
        {1: {"customer_name":"clientA", "order_items":{"Burger":1,"Pasta":2},"status":"Delivered"}, 2: {"customer_name":"clientB", "order_items":{"Salad":2,"Sushi":4, "Beverages":6, "Bakery":2},"status":"Placed"}}
        """
        if order_id in self.orders_log and self.orders_log[order_id]["status"] != "Picked Up":
            del self.orders_log[order_id]
        return self.orders_log

# create a menu

menu_1 = FoodDeliverySystem()
print(menu_1.display_menu())
# Explica el fragmento de codigo anterior:
# Se crea una instancia de la clase FoodDeliverySystem, es decir, se crea un objeto 
# que tiene acceso a los metodos y atributos de la clase FoodDeliverySystem.
# Se imprime el menu de la instancia menu_1, el cual es un diccionario que contiene
# los platillos y sus precios ordenados de menor a mayor precio.




