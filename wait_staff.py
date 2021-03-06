from dataclasses import dataclass
from employee import Employee
from table import Table
import datetime
from booking import Booking
from user import User
#from database import Database


class WaitStaff(Employee):
    def assign_customer_to_table(database):
        #does customer have booking
        while True:
            response = input("Does customer have booking?[y/n] ")
            if response.lower() == 'y':
                if WaitStaff.assign_customer_to_booked_table(database):
                    break
                else:
                    print("Invalid booking information")
            elif response.lower() == 'n':
                WaitStaff.assign_customer_to_unbooked_table(database)
                break


    # will assign a customer to a tablebooked table and will return success
    def assign_customer_to_booked_table(database) -> bool:
        name = input("Enter booking name: ")
        bookings = database.get_bookings()
        possible_bookings = list(filter(lambda x: x.name == name, bookings))
        if len(possible_bookings) == 0:
            return False
        elif len(possible_bookings) == 1:
            database.change_table_state(possible_bookings[0].table, "occupied")
            print(name + " has been successfullty assigned to table " + str(possible_bookings[0].table))
            return True
        else:
            print("Select booking")
            for booking in possible_bookings:
                print("Booking id " + str(booking.id) + ", time " + str(booking.time) + ", table " + str(booking.table))
            booking_id = int(input("Enter booking id: "))
            booking = list(filter(lambda x: x.id == booking_id, possible_bookings))
            if len(booking) == 0:
                return False
            else:
                database.change_table_state(booking[0].table, "occupied")
                print(name + " has been successfullty assigned to table " + str(possible_bookings[0].table))
                return True


    def assign_customer_to_unbooked_table(database):
        print("Select table")
        tables = database.get_avaliable_tables(datetime.datetime.now(), 5400)

        Table.display_table(tables)
        while True:
            table_id = int(input("Table: "))
            table = list(filter(lambda x: x.id == table_id, tables))
            if len(table) == 1:
                database.change_table_state(table[0].id, "occupied")
                print("customer has been successfullty assigned to table " + str(table[0].id))
                break

    def edit_booking(database):
        bookings = database.get_bookings()
        Booking.show_bookings(bookings)
        while True:
            booking_id = int(input("Enter booking id: "))

            booking = list(filter(lambda x: x.id == booking_id, bookings))
            if len(booking) == 1:
                break
            else:
                print("Invalid booking id")

        database.edit_booking(User.create_booking_with_id(database, booking_id))

        print("successfully updated booking " + str(booking_id))

    def delete_booking(database):
        bookings = database.get_bookings()
        Booking.show_bookings(bookings)

        while True:
            booking_id = int(input("Enter booking id: "))

            booking = list(filter(lambda x: x.id == booking_id, bookings))
            if len(booking) == 1:
                break
            else:
                print("Invalid booking id")

        database.delete_booking(booking_id)
        print("successfully deleted booking " + str(booking_id))

    def create_order(database, order_item, table_number):
        database.create_order(order_item, int(table_number))

    def modify_order(database):
        order_id = input("Enter order id: ")
        item_id = input("Enter item ids (with , in between) [if none, type 'none']: ")
        table_id = input("Enter table id: [if none, type 'none']: ")
        if item_id == 'none':
            item_id = None
        if table_id == 'none':
            table_id = None
        database.edit_order(int(order_id),
                            list(item_id.split(',')) if item_id is not None else None,
                            int(table_id) if table_id is not None else None, 
                            None)

    def delete_order(database):
        order_id = input("Enter order id: ")
        if order_id.isnumeric():
            database.delete_order(int(order_id))

    def deliver_item(database):
        order_number = input("Enter Order Number: ")
        order = database.get_order(order_number)
        order.change_state(database, 4)

    def clean_table(database):
        tables = database.get_occupied_tables()
        if len(tables) == 0:
            print("No tables need cleaning")
            return
        else:
            print("Tables to clean: ")

        Table.display_table(tables)

        while True:
            table_id = int(input("Enter table id: "))

            table = list(filter(lambda x: x.id == table_id, tables))
            if len(table) == 1:
                break
            else:
                print("Invalid table id")

        database.change_table_state(table_id, "free")
        print("table " + str(table_id) + " is clean and is now marked as 'free'")
