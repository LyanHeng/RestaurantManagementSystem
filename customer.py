from menu import Menu
from booking import Booking
from take_away_order import TakeAwayOrder
from order import Order
from payment import Payment
from user import User

class Customer(User):
    def __init__(self, name):
        super(self, name)

    # create a new booking
    def create_booking(self):
        return

    # get online menu
    def get_online_menu():
        return

    # create takeaway order
    def create_takeaway_order(self):
        return

    # pay takeaway order
    def pay_for_takeaway_order(self):
        return