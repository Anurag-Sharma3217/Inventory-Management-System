import classfile as cl

def save_file(storage, file_name):
    file = open(file_name, "w")
    for line in storage.items:
        file.write(f"{line.name} {line.price} {line.quantity}\n")
    file.close()

def load_file(file_name, storage):
    file = open(file_name, "r")
    for line in file:
        line = line.split()
        new_items = cl.Item(line[0], int(line[1]), int(line[2]))
        storage.add_item(new_items)
    file.close()

