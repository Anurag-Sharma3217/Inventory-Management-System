def get_name(message):

    while True:

        name = input(message)
        if name.replace(" ", "").isalpha():
            break
        print("Enter letters only.")

    return name

def get_number(message):
    while True:
        try:
            number = int(input(message))
            return number
            break
        except ValueError:
            print("Enter number only.")

def find_item(storage, item):
    if item.lower() in storage.lower():
        return storage
    return None
