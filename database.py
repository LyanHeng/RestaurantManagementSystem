from asyncio.windows_events import NULL
import json 
from os.path import exists
from menu import Menu
from item import Item
from order import Order

class Database:
    # file names
    DB_FOLDER = 'database//'
    ITEMS_FILE = DB_FOLDER + 'items.json'
    ORDERS_FILE = DB_FOLDER + 'orders.json'

    # opens json file and returns the JSON file as a dictionary
    def open_file(self, file_name):
        file = open(file_name)
        data = json.load(file)
        file.close()
        return data

    # will write a dictionary file into a json file
    def write_to_file(self, data, file_name):
        file = open(file_name, "w")
        file.write(json.dumps(data))
        file.close()

    def get_menu(self):
        menu_data = self.open_file(self.ITEMS_FILE)
        menu = Menu()
        for item in menu_data['items']:
            menu.items.append(Item(item['id'], item['name'], item['price'], item['ingredients']))
        return menu
    
    def create_menu_item(self, item):
        menu_data = {}
        if exists(self.ITEMS_FILE):
            menu_data = self.open_file(self.ITEMS_FILE)
        else:
            menu_data = {'items': []}
        menu_data['items'].append({
            'id': item.id,
            'name': item.name,
            'price': item.price,
            'ingredients': item.ingredients
            })
        self.write_to_file(menu_data, self.ITEMS_FILE)

    def edit_menu_item(self, item):
        menu_data = self.open_file(self.ITEMS_FILE)
        for i in range(len(menu_data['items'])):
            if menu_data['items'][i]['id'] == item.id:
                menu_data['items'][i] = {
                    'id': item.id,
                    'name': item.name,
                    'price': item.price,
                    'ingredients': item.ingredients
                    }
        
        self.write_to_file(menu_data, self.ITEMS_FILE)

    def delete_menu_item(self, item_id):
        menu_data = self.open_file(self.ITEMS_FILE)
        data = {}

        for i in range(len(menu_data['items'])):
            if menu_data['items'][i]['id'] == item_id:
                data = menu_data['items'][i]

        menu_data['items'].remove(data)
        self.write_to_file(menu_data, self.ITEMS_FILE)

    # get item details given an item id
    def get_item(self, item_id):
        items_data = self.open_file(self.ITEMS_FILE)
        for i in range(len(items_data['items'])):
            if items_data['items'][i]['id'] == int(item_id):
                item_object = items_data['items'][i]
                itemRequested = Item(item_object['id'], item_object['name'], item_object['price'], item_object['ingredients'])
                return itemRequested
        return NULL

    def get_tables():
        return

    def get_avaliable_tables():
        return

    def create_table():
        return
    
    def edit_table():
        return

    def delete_table():
        return

    def find_emplyee():
        return

    def get_emplyees():
        return

    def create_emplyee():
        return
    
    def edit_emplyee():
        return

    def delete_emplyee():
        return

    def get_bookings():
        return

    def create_booking():
        return

    def edit_booking():
        return

    def delete_booking():
        return

    # return order details given an order id
    def get_order(self, order_id):
        order_data = self.open_file(self.ORDERS_FILE)
        for i in range(len(order_data['orders'])):
            if order_data['orders'][i]['id'] == int(order_id):
                order_object = order_data['orders'][i]
                orderRequested = Order(order_object['id'], order_object['item_ids'], order_object['table_id'])
                return orderRequested
        return NULL

    def create_order():
        return

    def edit_order():
        return

    def delete_order():
        return