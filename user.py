#from database import Database
from booking import Booking
from table import Table
import datetime

class User():
    def __init__(self, name):
        self.name = name

    # create a new booking
    @staticmethod
    def create_booking(database):
        name = input("Customer name: ")
        # get the booking time
        date_str = input("Booking date [yyyy-mm-dd]: ")
        time_str = input("Booking time [hh:mm]: ")
        year, month, day = map(int, date_str.split('-'))
        hour, minute = map(int, time_str.split(':'))
        time = datetime.datetime(year, month, day, hour, minute)

        print("Avaliable tables: ")
        avaliable_tables = database.get_avaliable_tables(time, 5400) # 90 minute buffer time
        Table.display_table(avaliable_tables) 

        while True:
            table_id = int(input("Enter table number: "))
            if len(list(filter(lambda x: x.id == table_id, avaliable_tables))) > 0:
                break
            else:
                print("invalid table number")

        booking = Booking(database.generate_id(database.BOOKINGS_FILE), name, time, table_id)
        database.create_booking(booking)

    # edit an existing booking
    @staticmethod
    def edit_booking(self, booking):
        return

    # cancel an existing booking
    @staticmethod
    def cancel_booking(self, booking):
        return