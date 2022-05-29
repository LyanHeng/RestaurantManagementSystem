from collections import namedtuple
from item import Item

class Menu():
    def __init__(self):
        self.items = []
    
    #display items currently in the menu with format
    def display_item(menu):
        MenuEntry = namedtuple('MenuEntry', ['id','name','price', 'ingredients'])
        _menu = []
        for item in menu:
            _menu.append(MenuEntry(item.id, item.name, item.price, item.ingredients))

        for entry in _menu:
            id = str(getattr(entry,'id')).ljust(5)
            name = str(getattr(entry,'name')).ljust(25)
            price = '$' + str(getattr(entry,'price')).ljust(10)
            ingredients = str(getattr(entry,'ingredients')).ljust(7)
            print('{0}{1}{2}{3}'.format(id,name,price,ingredients))