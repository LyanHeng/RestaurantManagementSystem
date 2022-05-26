from card_payment import CardPayment
from cash_payment import CashPayment
from database import Database
from item import Item
from payment import Payment
from table import Table
from booking import Booking
from user import User
import json
from wait_staff import WaitStaff 

def main():
    # this should be the only database object created (singleton)
    database = Database()
    
    ######################## workflow for order ##############################
    # delete current menu
    for item in database.get_menu().items:
        database.delete_menu_item(item.id)

    database.create_menu_item(Item(database.generate_id(database.ITEMS_FILE), "Test1", 10, ["ingredient1", "ingredient2", "ingredient3"]))
    database.create_menu_item(Item(database.generate_id(database.ITEMS_FILE), "Test2", 10, ["ingredient1", "ingredient2"]))
    database.create_menu_item(Item(database.generate_id(database.ITEMS_FILE), "Test3", 10, ["ingredient1", "ingredient2", "ingredient3", "ingredient4"]))

    database.edit_menu_item(Item(1, "Testchange3", 90, ["ingredient1", "ingredient2", "ingredient3", "ingredient4", "ingredient5"]))

    database.delete_menu_item(2)

    # delete current tables
    for table in database.get_tables():
        database.delete_table(table.id)

    database.create_table(Table(1, 4, "free"))
    database.create_table(Table(2, 4, "free"))
    database.create_table(Table(3, 4, "free"))
    database.create_table(Table(4, 4, "free"))

    database.edit_table(Table(4, 6, "free"))

    # delete current booking
    for booking in database.get_bookings():
       database.delete_booking(booking.id)

    database.create_booking(Booking(1, "Bob", 0, 1))
    database.create_booking(Booking(2, "Fred", 0, 1))
    database.create_booking(Booking(3, "Mary", 0, 1))
    database.create_booking(Booking(4, "Jane", 0, 1))

    database.edit_booking(Booking(3, "john", 0, 1))

    print("Create Booking")
    User.create_booking()
    print("Create Booking 2")
    User.create_booking()

    print("assign Customer to table")
    WaitStaff.assign_customer_to_table()
    print("assign Customer to table 2")
    WaitStaff.assign_customer_to_table()

    ######################## workflow for payment ##############################
    payment = Payment(database, None)
    amount_due = payment.create_transaction()
    if amount_due != -1:
        while payment.retry_payment():
            print("The amount due for payment is: " + str(amount_due))
            payment_method = input("Pay by card or cash? (card/cash/exit): ")
            # determines payment method
            if payment_method == "card":
                payment = CardPayment(database, payment.order)
            elif payment_method == "cash":
                payment = CashPayment(database, payment.order)
            elif payment_method == "exit":
                payment.state = "Failed"
                print(payment.state)
                continue
            else:
                print("Please enter card/cash/exit")
                continue
            payment.state = payment.process_payment()
            # print invoice if success, offers retry if failed
            if payment.state == "Success":
                payment.print_invoice(True) if type(payment) == CashPayment else payment.print_invoice(False)
            print(payment.state)
    print("Payment completed/exited")

if __name__ == "__main__":
    main()