import json
from utils import get_positive_int
from inventory import InventoryManager

CART_FILE = 'cart.json'

class CartManager:
    def __init__(self):
        self.cart_data = self.load_cart()

    def load_cart(self):
        try:
            with open(CART_FILE, 'r') as file:
                cart_data = json.load(file)
            return cart_data
        except FileNotFoundError:
            return []

    def save_cart(self):
        with open(CART_FILE, 'w') as file:
            json.dump(self.cart_data, file, indent=2)

    def view_cart(self):
        if not self.cart_data:
            print("Cart is empty.")
        else:
            print("Current cart:")
            for item in self.cart_data:
                print(f"{item['name']}: quantity - {item['quantity']}")
    def remove_from_cart(self, inventory_manager):
        self.view_cart()

        item_name = input("Enter the name of the product to remove from the cart: ")

        for item in self.cart_data:
            if item['name'].lower() == item_name.lower():
                quantity_to_remove = get_positive_int(f"Enter the quantity of '{item_name}' to remove from the cart: ")

                if quantity_to_remove <= item['quantity']:
                    item['quantity'] -= quantity_to_remove

                    for product in inventory_manager.inventory_data:
                        if product['name'].lower() == item_name.lower():
                            product['quantity'] += quantity_to_remove
                            break

                    inventory_manager.save_inventory()
                    self.save_cart()

                    print(f"{quantity_to_remove} units of '{item_name}' removed from the cart.")
                    if item['quantity'] == 0:
                        self.cart_data.remove(item)
                        print(f"Notification: '{item_name}' removed from the cart.")
                    break
                else:
                    print(f"Requested quantity exceeds the available quantity in the cart.")
                break
        else:
            print(f"Product '{item_name}' not found in the cart.")

    def add_to_cart(self, inventory_manager):
        inventory_manager.view_inventory()

        item_name = input("Enter the name of the product to add to the cart: ")

        for product in inventory_manager.inventory_data:
            if product['name'].lower() == item_name.lower():
                quantity_available = product['quantity']

                if quantity_available > 0:
                    quantity_to_add = get_positive_int(f"Enter the quantity of '{item_name}' to add to the cart: ")

                    if quantity_to_add <= quantity_available:
                        for item in self.cart_data:
                            if item['name'].lower() == item_name.lower():
                                item['quantity'] += quantity_to_add
                                if item['quantity'] <= 0:
                                    self.cart_data.remove(item)
                                    print(f"Notification: '{item_name}' removed from the cart.")
                                break
                        else:
                            self.cart_data.append({'name': item_name, 'quantity': quantity_to_add})

                        product['quantity'] -= quantity_to_add
                        print(f"{quantity_to_add} units of '{item_name}' added to the cart.")
                        inventory_manager.save_inventory()
                        self.save_cart()
                    else:
                        print(f"Available quantity of '{item_name}' is less than requested.")
                else:
                    print(f"No more available quantity of '{item_name}'.")
                break
        else:
            print(f"Product '{item_name}' not found in inventory.")


