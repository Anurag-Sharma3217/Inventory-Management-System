class Item:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:

    def __init__(self, items):
        self.items = items

    def add_item(self, items):
        self.items.append(items)

    def show_item(self):
        for item in self.items:
            print(f"\nItem name: {item.name}")
            print(f"Item price: {item.price}")
            print(f"Item quantity: {item.quantity}\n")

    def find_item(self, search):
        for item in self.items:
            if search.lower() in item.name.lower():
                print(item.name, item.price, item.quantity, "\n")
                return
        else:
            print("Item not found.")

    def remove_item(self, it):
        for item in self.items:
            if it.lower() in item.name.lower():
                self.items.remove(item)
                print("Item deleted")
                return
        else:
            print("Item not found.")

    def update_price(self, it, price):
        for item in self.items:
            if it.lower() in item.name.lower():
                item.price = price
                print("Price updated.")
                return
        else:
            print("Item not found.")

    def update_quantity(self, it, quantity):
        for item in self.items:
            if it.lower() in item.name.lower():
                item.quantity = quantity
                print("Quantity updated.")
                return
        else:
            print("Item not found.")

    def inventory_summary(self):
        value = 0
        for item in self.items:
            value += item.price*item.quantity
        print(f"Total inventory value: {value}")
        print(f"Total items: {len(self.items)}")
        