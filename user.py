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
        time = input("Booking time: ")
        table = input("Table: ")

        booking = Booking(database.generate_id(database.BOOKINGS_FILE), name, time, table)
        database.create_booking(booking)

    # edit an existing booking
    @staticmethod
    def edit_booking(self, booking):
        return

    # cancel an existing booking
    @staticmethod
    def cancel_booking(self, booking):
        return