from employee import Employee
from database import Database

class WaitStaff(Employee):
    def assign_customer_to_table():
        #does customer have booking
        while True:
            response = input("Does customer have booking?[y/n] ")
            if response.lower() == 'y':
                if WaitStaff.assign_customer_to_booked_table():
                    break
                else:
                    print("Invalid booking information")
            elif response.lower() == 'n':
                WaitStaff.assign_customer_to_unbooked_table()
                break


    # will assign a customer to a tablebooked table and will return success
    def assign_customer_to_booked_table() -> bool:
        database = Database()
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


    def assign_customer_to_unbooked_table():
        print("Select table")
        print(WaitStaff.display_tables())

        database = Database()
        tables = database.get_tables()
        while True:
            table_id = int(input("Table: "))
            table = list(filter(lambda x: x.id == table_id, tables))
            if len(table) == 1:
                database.change_table_state(table[0].id, "occupied")
                break


    def create_order():
        pass

    def modify_order():
        pass

    def delete_order():
        pass

    def deliver_item():
        pass

    def clean_table():
        pass

    def set_table_state(self):
        id = input("Enter table id: ")  
        #table does not exist in database
        table = Database.get_tables(id)
        if not table:
            print("Table does not exist")
            return -1
        table.state = input("Enter table state [free/occupied]: ") 
    