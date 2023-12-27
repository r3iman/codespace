import json
from datetime import datetime
from inventory import InventoryManager
from cart import CartManager
from utils import get_positive_int

SALES_FILE = 'sales.json'

class SalesManager:
    def __init__(self):
        self.sales_data = self.load_sales()

    def load_sales(self):
        try:
            with open(SALES_FILE, 'r') as file:
                sales_data = json.load(file)
            return sales_data
        except FileNotFoundError:
            return []

    def save_sales(self):
        with open(SALES_FILE, 'w') as file:
            json.dump(self.sales_data, file, indent=2)

    def make_sale(self, inventory_manager, cart_manager):
        inventory_manager.load_inventory()
        cart_manager.view_cart()

        items = self.get_sale_items(cart_manager.cart_data)
        for item in items:
            product_name = item['name']
            sale_quantity = item['quantity']

            for product in inventory_manager.inventory_data:
                if product['name'].lower() == product_name.lower():
                    quantity_available = product['quantity']
                    if quantity_available > 0 and sale_quantity <= quantity_available:
                        sale_amount = sale_quantity * product['price']

                        sale = {
                            'product_name': product_name,
                            'quantity': sale_quantity,
                            'amount': sale_amount,
                            'timestamp': str(datetime.now())
                        }

                        self.sales_data.append(sale)
                        product['quantity'] -= sale_quantity

                        for cart_item in cart_manager.cart_data:
                            if cart_item['name'].lower() == product_name.lower():
                                cart_item['quantity'] -= sale_quantity
                                if cart_item['quantity'] == 0:
                                    cart_manager.cart_data.remove(cart_item)
                                break

                        inventory_manager.save_inventory()
                        self.save_sales()
                        cart_manager.save_cart()
                        print(f"Operation (sell) with '{product_name}' done.")
                        break
                    else:
                        print(f"Available amount of '{product_name}' lower than we have")
                        break
            else:
                print(f"Product '{product_name}' not found in inventory.")
        print("Notification: Cart is empty.")
  

    def get_sale_items(self, cart_data):
        items = []
        while True:
            item = self.get_sale_item()
            if not item:
                break
            items.append(item)
        return items

    def get_sale_item(self):
        item_name = input("Enter the name of the product (or type 'done' to finish): ")
        if item_name.lower() == 'done':
            return None

        quantity = int(input(f"Enter the quantity of '{item_name}': "))

        return {'name': item_name, 'quantity': quantity}

    def generate_sales_report(self):
        if not self.sales_data:
            print("No sales data available.")
            return

        total_sales = 0
        print("Sales Report:")
        for sale in self.sales_data:
            print(f"Product: {sale['product_name']}, Quantity: {sale['quantity']}, Amount: ${sale['amount']}")
            total_sales += sale['amount']

        print(f"\nTotal Sales: ${total_sales}")
