from asyncio.windows_events import NULL
import json
from os.path import exists
from menu import Menu
from item import Item
from order import Order
from table import Table
from booking import Booking


class Database(object):
    # define as singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Database, cls).__new__(cls)
        return cls.instance

    # file names
    DB_FOLDER = 'database//'
    ITEMS_FILE = DB_FOLDER + 'items.json'
    ORDERS_FILE = DB_FOLDER + 'orders.json'
    TABLES_FILE = DB_FOLDER + 'tables.json'
    EMPLOYEES_FILE = DB_FOLDER + 'employees.json'
    BOOKINGS_FILE = DB_FOLDER + 'bookings.json'

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

    # will generate the lowest unique ID for the specific table
    def generate_id(self, file_name):
        data = self.open_file(file_name)
        id = 0
        items = list(data.values())[0]
        items = sorted(items, key=lambda d: d['id'])
        for item in items:
            if item['id'] == id:
                id += 1

        #print("generated id " + str(id))
        return id

    def get_menu(self):
        menu_data = self.open_file(self.ITEMS_FILE)
        menu = Menu()
        for item in menu_data['items']:
            menu.items.append(
                Item(item['id'], item['name'], item['price'], item['ingredients']))
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
        items_data = self.open_file(self.ITEMS_FILE)
        for i in range(len(items_data['items'])):
            if items_data['items'][i]['id'] == int(item_id):
                item_object = items_data['items'][i]
                itemRequested = Item(
                    item_object['id'], item_object['name'], item_object['price'], item_object['ingredients'])
                return itemRequested
        return NULL

    def get_table(self, table_id):
        tables_data = self.open_file(self.TABLES_FILE)
        for i in range(len(tables_data['tables'])):
            if tables_data['tables'][i]['id'] == int(table_id):
                table_object = tables_data['tables'][i]
                tableRequested = Table(
                    table_object['id'], table_object['size'], table_object['state'])
                return tableRequested
        return NULL

    def get_tables(self):
        table_data = self.open_file(self.TABLES_FILE)
        tables = []
        for table in table_data['tables']:
            tables.append(Table(table['id'], table['size'], table['state']))
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
            'size': table.size,
            'state': table.state
        })
        self.write_to_file(table_data, self.TABLES_FILE)

    def change_table_state(self, table_id, state):
        # find table with matching id
        tables = self.get_tables()
        table = list(filter(lambda x: x.id == table_id, tables))
        if len(table) == 0:
            raise Exception("No tables with ID " + str(table_id))
        table[0].state = state
        self.edit_table(table[0])

    def edit_table(self, table):
        table_data = self.open_file(self.TABLES_FILE)
        for i in range(len(table_data['tables'])):
            if table_data['tables'][i]['id'] == table.id:
                table_data['tables'][i] = {
                    'id': table.id,
                    'size': table.size,
                    'state': table.state
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
            employees.append(
                Table(employee_data['id'], employee_data['size'], "free"))
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
            bookings.append(
                Booking(booking['id'], booking['name'], booking['time'], booking['table_id']))
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

    def get_orders(self):
        orders = []
        tables = self.get_tables()
        order_data = self.open_file(self.ORDERS_FILE)
        for i in range(len(order_data['orders'])):
            order_object = order_data['orders'][i]
            print(order_object)
            for table in tables:
                if table.id == order_object['table_id']:
                    order = Order(order_data['orders'][i]['id'], table)
                    for item_id in order_object['item_ids']:
                        order.add_item(self.get_item(item_id))
                    orders.append(order)
                    break
        return orders

    # return order details given an order id
    def get_order(self, order_id):
        order_data = self.open_file(self.ORDERS_FILE)
        for i in range(len(order_data['orders'])):
            if order_data['orders'][i]['id'] == int(order_id):
                order_object = order_data['orders'][i]
                tables = self.get_tables()
                for table in tables:
                    if table.id == order_object['table_id']:
                        orderRequested = Order(order_id, table)
                        for item_id in order_object['item_ids']:
                            orderRequested.add_item(self.get_item(item_id))
                        return orderRequested
        return NULL

    def create_order(self, items, table_number):
        order_data = {}
        if exists(self.ORDERS_FILE):
            order_data = self.open_file(self.ORDERS_FILE)
        else:
            order_data = {'orders': []}
        order_data['orders'].append({
            'id': self.generate_id(self.ORDERS_FILE),
            'items_id': items,
            'table_id': table_number
        })
        print(order_data)
        self.write_to_file(order_data, self.ORDERS_FILE)

    def edit_order():
        return

    def delete_order():
        return
