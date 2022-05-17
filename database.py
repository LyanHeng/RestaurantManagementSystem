import json 
from os.path import exists
from menu import Menu
from item import Item

class Database:
    # file names
    ITEMS_FILE = 'items.json'

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
        menu_data = self.__open_file(self.ITEMS_FILE)
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

    def get_tables():
        pass

    def get_avaliable_tables():
        pass

    def create_table():
        pass
    
    def edit_table():
        pass

    def delete_table():
        pass

    def find_emplyee():
        pass

    def get_emplyees():
        pass

    def create_emplyee():
        pass
    
    def edit_emplyee():
        pass

    def delete_emplyee():
        pass

    def get_bookings():
        pass

    def create_booking():
        pass

    def edit_booking():
        pass

    def delete_booking():
        pass

    def get_order():
        pass

    def create_order():
        pass

    def edit_order():
        pass

    def delete_order():
        pass