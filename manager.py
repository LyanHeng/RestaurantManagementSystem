from employee import Employee
from item import Item
from table import Table


class Manager(Employee):
    # create a new item
    def create_item(database):
        name = input("Enter item name: ")
        price = input("Enter item price: ")
        ingredients = []
        while True:
            user_input = input(
                "Enter item ingredient [type 'done' when finish]: ")
            x = user_input.split(', ')
            for ingredient in x:
                if ingredient != 'done':
                    ingredients.append(ingredient)
                else:
                    item = Item(database.generate_id(
                        database.ITEMS_FILE), name, price, ingredients)
                    database.create_menu_item(item)
                    return

    # edit item

    def edit_item(database):
        id = input("Enter item id: ")

        # item does not exist in database
        item = database.get_item(id)
        if not item:
            print("Item does not exist")
            return -1

        item.name = input("Enter new item name: ")
        item.price = input("Enter new item price: ")
        item.ingredients = []
        while True:
            user_input = input(
                "Enter new item ingredient [type 'done' when finish]: ")
            x = user_input.split(', ')
            for ingredient in x:
                if ingredient != 'done':
                    item.ingredients.append(ingredient)
                else:
                    database.edit_menu_item(item)
                    return

    # delete item
    def delete_item(database):
        id = input("Enter item id: ")
        # item does not exist in database
        item = database.get_item(id)
        if not item:
            print("Item does not exist")
            return -1
        database.delete_menu_item(int(id))

    def create_new_table(database):
        size = input("Enter table size: ")
        state = input("Enter table state [free/occupied]: ")

        table = Table(database.generate_id(database.TABLES_FILE), size, state)
        database.create_table(table)

    def edit_existing_table(database):
        id = input("Enter table id: ")
        # table does not exist in database
        table = database.get_table(int(id))
        if not table:
            print("Table does not exist")
            return -1

        table.size = input("Enter table new size: ")
        table.state = input("Enter table new state [free/occupied]: ")

        database.edit_table(table)

    def delete_existing_table(database):
        id = input("Enter table id: ")
        # table does not exist in database
        table = database.get_table(int(id))
        if not table:
            print("Table does not exist")
            return -1
        database.delete_table(int(id))

    def free_table(database):
        id = input("Enter table id: ")
        # table does not exist in database
        table = database.get_table(int(id))
        if not table:
            print("Table does not exist")
            return -1
        table.state = 'free'
        database.edit_table(table)

    def create_employee():
        pass

    def edit_employee():
        pass

    def delete_employee():
        pass
