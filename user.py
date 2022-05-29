#from database import Database
from booking import Booking

class User():
    def __init__(self, name):
        self.name = name

    # create a new booking
    @staticmethod
    def create_booking(database):
        name = input("Customer name: ")
        # get the booking time
        time = input("Booking time: ")

        booking = Booking(database.generate_id(database.BOOKINGS_FILE), name, time, 0)
        database.create_booking(booking)

    # edit an existing booking
    @staticmethod
    def edit_booking(self, booking):
        return

    # cancel an existing booking
    @staticmethod
    def cancel_booking(self, booking):
        return