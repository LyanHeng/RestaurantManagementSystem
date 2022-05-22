from order import Order
from collections import namedtuple
from item import Item
from database import Database

class StatisticAnalysis():
    def __init__(self):
        return

    #display items currently in the menu with format
    def display_stat(self):
        ItemList = namedtuple('ItemList', ['id','name','total_sale_of_item'])
        _item = []
        for item in Database.get_menu():
            _item.append(ItemList(item.id, item.name, self.calculate_sales_of_item(item.id)))

        for entry in _item:
            id = str(getattr(entry,'id')).ljust(5)
            name = str(getattr(entry,'name')).ljust(25)
            total_sale_of_item = str(getattr(entry,'total_sale_of_item')).ljust(7)
            print ('{0}{1}{2}'.format(id,name,total_sale_of_item))

    #Calculate total sales of each item
    def calculate_sales_of_item(self, item_id):
        total = 0
        #loop through all orders
        for order in Database.ORDERS_FILE:
            #loop through all items in order
            for item in order:
                item = Database.get_item(item_id)
            # this should never happen if application creates item objects properly
            if not item:
                print("Unexpected Error: item does not exist in database")
                continue
            if item.id == item_id:
                total += item.price
        return total

    #Calculate total sales over time (per day, per month)
    def calculate_sales_over_time():
        return