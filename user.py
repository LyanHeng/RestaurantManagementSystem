from database import Database
from booking import Booking

class User():
    def __init__(self, name):
        self.name = name

    # create a new booking
    @staticmethod
    def create_booking():
        database = Database()

        name = input("Customer name: ")
        # get the booking time
        time = input("Booking time: ")
        # display all avaliable tables 
        print (User.display_tables())
        table = int(input("Table: "))
        # test if table is free and exists 

        booking = Booking(database.generate_id(database.BOOKINGS_FILE), name, time, table)
        database.create_booking(booking)

    def display_tables():
        tables = Database().get_tables()
        string = "tables: \n"
        for table in tables:
            string += "\ttable " + str(table.id) + ", size " + str(table.size) + "\n"
        return string

    # edit an existing booking
    @staticmethod
    def edit_booking(self, booking):
        return

    # cancel an existing booking
    @staticmethod
    def cancel_booking(self, booking):
        return