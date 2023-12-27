from cart import CartManager
from inventory import InventoryManager
from sales import SalesManager
from utils import get_choice

def main():
    cart_manager = CartManager()
    inventory_manager = InventoryManager()
    sales_manager = SalesManager()

    while True:
        print("1. Add product to cart")
        print("2. Remove product from cart")
        print("3. Change inventory")
        print("4. Add product")
        print("5. Make sale")
        print("6. Sales report")
        print("7. Exit")

        choice = get_choice()

        if choice == 1:
            cart_manager.add_to_cart(inventory_manager)
        elif choice == 2:
            cart_manager.remove_from_cart(inventory_manager)        
        elif choice == 3:
            inventory_manager.edit_product()
        elif choice == 4:
            inventory_manager.add_product()
        elif choice == 5:
            sales_manager.make_sale(inventory_manager, cart_manager)
        elif choice == 6:
            sales_manager.generate_sales_report()
        elif choice == 7:
            print("The end.")
            break
        else:
            print("Incorrect choice, try again later.")

if __name__ == "__main__":
    main()
