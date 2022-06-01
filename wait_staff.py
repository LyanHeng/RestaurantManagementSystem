from employee import Employee
from table import Table

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
                return True


    def assign_customer_to_unbooked_table(database):
        print("Select table")
        Table.display_table(database.get_tables())

        tables = database.get_tables()
        while True:
            table_id = int(input("Table: "))
            table = list(filter(lambda x: x.id == table_id, tables))
            if len(table) == 1:
                database.change_table_state(table[0].id, "occupied")
                break


    def create_order(database, items, table_number):
        database.create_order(items, int(table_number))
        # TODO: send order to kitchen
        pass

    def modify_order():
        pass

    def delete_order():
        pass

    def deliver_item(database):
        order_number = input("Enter Order Number: ")
        order = database.get_order(order_number)
        order.change_state(database, order._states[2])
        print("Order Delivered!")

    def clean_table(database, order):
        order.change_state(database, order._states[6])
        database.change_table_state(order.table.id, "free")
        order.close_order()
