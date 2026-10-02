import classfile as cl, utils as u

def menu():
    print('''\n------Inventory Management System------
_______________________________________\n\n''')
    print('''1. Add item
2. View item
3. Find item
4. Remove item
5. Update price
6. Update quantity
7. Inventory summary
8. Exit\n''')
    choice = u.get_number("Enter choice: ")
    return choice

def create_items(storage):
    name = u.get_name("Enter item's name: ")
    price = u.get_number("Enter itme's price: ")
    quantity = u.get_number("Enter item's quantity: ")
    item = cl.Item(name, price, quantity)
    storage.add_item(item)
    print("item added.")

def view(storage):
    storage.show_item()

def find_item(storage):
    search = u.get_name("Enter item's name: ")
    cl.Inventory.find_item(storage, search)

def remove_items(storage):
    it = u.get_name("Enter item's name: ")
    cl.Inventory.remove_item(storage, it)

def updates_price(storage):
    it = u.get_name("Enter item's name: ")
    price = u.get_number("Enter item's new price: ")
    cl.Inventory.update_price(storage, it, price)

def updates_quantity(storage):
    it = u.get_name("Enter item's name: ")
    quantity = u.get_number("Enter item's new quantity: ")
    cl.Inventory.update_quantity(storage, it, quantity)

def Inventory_summary(storage):
    cl.Inventory.inventory_summary(storage)

def exit_program():
    print("Thank you for using.")

def invalid():
    print("Invalid options")