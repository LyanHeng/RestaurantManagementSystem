import json 
from os.path import exists
from menu import Menu
from item import Item
from table import Table
from booking import Booking

class Database:
    # file names
    ITEMS_FILE = 'items.json'
    TABLES_FILE = 'tables.json'
    EMPLOYEES_FILE = 'employees.json'
    BOOKINGS_FILE = 'bookings.json'
    ORDERS_FILE = 'orders.json'

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

    def generate_key(self, file_name):
        pass

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

    def get_item(self, item_id):
        pass

    def get_tables(self):
        table_data = self.open_file(self.TABLES_FILE)
        tables = []
        for table in table_data['tables']:
            tables.append(Table(table['id'], table['size'], "free"))
        return tables

    def get_avaliable_tables(self):
        pass

    def create_table(self, table):
        table_data = {}
        if exists(self.TABLES_FILE):
            table_data = self.open_file(self.TABLES_FILE)
        else:
            table_data = {'tables': []}
        table_data['tables'].append({
                'id': table.id,
                'size': table.size
            })
        self.write_to_file(table_data, self.TABLES_FILE)
    
    def edit_table(self, table):
        table_data = self.open_file(self.TABLES_FILE)
        for i in range(len(table_data['tables'])):
            if table_data['tables'][i]['id'] == table.id:
                table_data['tables'][i] = {
                        'id': table.id,
                        'size': table.size
                    }
        
        self.write_to_file(table_data, self.TABLES_FILE)

    def delete_table(self, table_id):
        table_data = self.open_file(self.TABLES_FILE)
        data = {}

        for i in range(len(table_data['tables'])):
            if table_data['tables'][i]['id'] == table_id:
                data = table_data['tables'][i]

        table_data['tables'].remove(data)
        self.write_to_file(table_data, self.TABLES_FILE)

    def find_employee():
        pass

    def get_employees(self):
        employee_data = self.open_file(self.EMPLOYEES_FILE)
        employees = []
        for employee in employee_data['tables']:
            employees.append(Table(table['id'], table['size'], "free"))
        return employees

    def create_employee():
        pass
    
    def edit_employee():
        pass

    def delete_employee():
        pass

    def get_bookings(self):
        booking_data = self.open_file(self.BOOKINGS_FILE)
        bookings = []
        for booking in booking_data['bookings']:
            bookings.append(Booking(booking['id'], booking['name'], booking['time'], booking['table_id']))
        return bookings

    def create_booking(self, booking):
        booking_data = {}
        if exists(self.BOOKINGS_FILE):
            booking_data = self.open_file(self.BOOKINGS_FILE)
        else:
            booking_data = {'bookings': []}
        booking_data['bookings'].append({
                'id': booking.id,
                'name': booking.name,
                'time': booking.time,
                'table_id': booking.table
            })
        self.write_to_file(booking_data, self.BOOKINGS_FILE)

    def edit_booking(self, booking):
        booking_data = self.open_file(self.BOOKINGS_FILE)
        for i in range(len(booking_data['bookings'])):
            if booking_data['bookings'][i]['id'] == booking.id:
                booking_data['bookings'][i] = {
                        'id': booking.id,
                        'name': booking.name,
                        'time': booking.time,
                        'table_id': booking.table
                    }
        
        self.write_to_file(booking_data, self.BOOKINGS_FILE)

    def delete_booking(self, booking_id):
        booking_data = self.open_file(self.BOOKINGS_FILE)
        data = {}

        for i in range(len(booking_data['bookings'])):
            if booking_data['bookings'][i]['id'] == booking_id:
                data = booking_data['bookings'][i]

        booking_data['bookings'].remove(data)
        self.write_to_file(booking_data, self.BOOKINGS_FILE)

    def get_order():
        pass

    def create_order():
        pass

    def edit_order():
        pass

    def delete_order():
        pass