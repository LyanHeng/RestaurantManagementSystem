from employee import Employee
from item import Item
from database import Database
from table import Table

class Manager(Employee):
    # create a new item
    def create_item(self):
        database = Database()

        name = input("Enter item name: ")
        price = input("Enter item price: ")
        ingredients = input("Enter item ingredients: ")

        item = Item(database.generate_id(database.ITEMS_FILE), name, price, ingredients)
        database.create_menu_item(item)
    
    #edit item
    def edit_item(self):
        id = input("Enter item id: ")
            
        #item does not exist in database
        item = Database.get_item(id)
        if not item:
            print("Item does not exist")
            return -1
            
        item.name = input("Enter new item name: ")
        item.price = input("Enter new item price: ")
        item.ingredients = input("Enter new item ingredients: ")

        Database.edit_menu_item(item)

    #delete item
    def delete_item(self):
        id = input("Enter item id: ")
        #item does not exist in database
        item = Database.get_item(id)
        if not item:
            print("Item does not exist")
            return -1
        Database.delete_menu_item(item)

    def create_new_table(self):
        database = Database()

        size = input("Enter table size: ")
        state = input("Enter table state [free/occupied]: ")

        table = Table(database.generate_id(database.TABLES_FILE), size, state)
        database.create_table(table)

    def edit_table(self):
        id = input("Enter table id: ")   
        #table does not exist in database
        table = Database.get_tables(id)
        if not table:
            print("Table does not exist")
            return -1
            
        table.size = input("Enter table new name: ")
        table.state = input("Enter table new state: ")

        Database.edit_table(table)

    def delete_table(self):
        id = input("Enter table id: ")  
        #table does not exist in database
        table = Database.get_tables(id)
        if not table:
            print("Table does not exist")
            return -1
        Database.delete_table(table)
        pass

    def create_employee():
        pass
    
    def edit_employee():
        pass

    def delete_employee():
        pass