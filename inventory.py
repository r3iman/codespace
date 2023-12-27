import json

INVENTORY_FILE = 'inventory.json'

class InventoryManager:
    def __init__(self):
        self.inventory_data = self.load_inventory()

    def load_inventory(self):
        try:
            with open(INVENTORY_FILE, 'r') as file:
                inventory_data = json.load(file)
            return inventory_data
        except FileNotFoundError:
            with open(INVENTORY_FILE, 'w') as file:
                json.dump([], file)
            return [] 
        except json.decoder.JSONDecodeError:
            return []

    def save_inventory(self):
        with open(INVENTORY_FILE, 'w') as file:
            json.dump(self.inventory_data, file, indent=2)

    def view_inventory(self):
        if not self.inventory_data:
            print("Empty inventory.")
        else:
            print("Actual inventory:")
            for product in self.inventory_data:
                print(f"{product['name']}: price - {product['price']}, amount - {product['quantity']}")

    def add_product(self):
        name = input("Set product name: ")
        price = float(input("Set product price: "))
        quantity = int(input("Set product quantity: "))

        new_product = {'name': name, 'price': price, 'quantity': quantity}
        self.inventory_data.append(new_product)

        self.save_inventory()
        print(f"Product '{name}' successfully added into inventory.")

    def edit_product(self):
        self.view_inventory()

        product_name = input("Which product do you want to change: ")

        for product in self.inventory_data:
            if product['name'].lower() == product_name.lower():
                new_price = float(input(f"Set new price '{product_name}': "))
                new_quantity = int(input(f"Set new amount '{product_name}': "))

                product['price'] = new_price
                product['quantity'] = new_quantity

                self.save_inventory()
                print(f"Information about '{product_name}' updated.")
                return

        print(f"Product '{product_name}' not found.")
