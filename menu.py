from collections import namedtuple
from item import Item
from database import Database

class Menu():
    def __init__(self):
        self.items = []
    
    #display items currently in the menu with format
    def display_item():
        MenuEntry = namedtuple('MenuEntry', ['id','name','price', 'ingredients'])
        _menu = []
        for item in Database.get_menu():
            _menu.append(MenuEntry(item.id, item.name, item.price, item.ingredients))

        for entry in _menu:
            id = str(getattr(entry,'id')).ljust(5)
            name = str(getattr(entry,'name')).ljust(25)
            price = str(getattr(entry,'price')).ljust(7)
            ingredients = str(getattr(entry,'ingredients')).ljust(7)
            print ('{0}{1}{2}{3}'.format(id,name,price,ingredients))

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

    def delete_item(self):
        id = input("Enter item id: ")
        #item does not exist in database
        item = Database.get_item(id)
        if not item:
            print("Item does not exist")
            return -1
        Database.delete_menu_item(item)