from database import Database
from booking import Booking
from user import User
from employee import Employee
from manager import Manager
from table import Table
from payment import Payment
from menu import Menu
from card_payment import CardPayment
from cash_payment import CashPayment
from wait_staff import WaitStaff

def show_menu(database):
    print("Cosy Kangaroo Menu: ")
    print()
    id = 'Id'.ljust(5)
    name = 'Name'.ljust(25)
    price = 'Price'.ljust(10)
    ingredients = 'Ingredients'.ljust(7)
    print('{0}{1}{2}{3}'.format(id, name, price, ingredients))
    Menu.display_item(database.get_menu().items)

def show_table(database):
    print("Current Tables: ")
    print()
    id = 'Id'.ljust(5)
    size = 'Size'.ljust(25)
    state = 'State'.ljust(10)
    print('{0}{1}{2}'.format(id, size, state))
    Table.display_table(database.get_tables())

def payment_handling(database):
    print("New Payment: ")
    print()
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
            print()
            input("Enter to continue.....")
            print()
    print("Payment completed/exited")
    # TODO: Edit table state

def manager_page(database):
    while True:
        print("================================================================")
        print("================================================================")
        print("Welcome manager")
        print("================================================================")
        print("================================================================")
        print()
        print("~~~~~~~~~~~ Item ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Display menu [type 'show_menu'].")
        print("Create a new item [type 'new_menu'].")
        print("Edit an existing item [type 'edit_menu'].")
        print("Delete an existing item [type 'delete_menu'].")
        print()
        print("~~~~~~~~~~~ Table ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Display all tables [type 'show_table'].")
        print("Create a new table [type 'new_table'].")
        print("Edit an existing table [type 'edit_table'].")
        print("Delete an existing table [type 'delete_table'].")
        print()
        print("~~~~~~~~~~~ Exit ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Exit [type 'exit'].")
        print()
        manager_input = input("Select an action: ")
        print()
        if manager_input == 'new_menu':
            Manager.create_item(database)
        elif manager_input == 'edit_menu':
            Manager.edit_item(database)
        elif manager_input == 'delete_menu':
            Manager.delete_item(database)
        elif manager_input == 'new_table':
            Manager.create_new_table(database)
        elif manager_input == 'edit_table':
            Manager.edit_existing_table(database)
        elif manager_input == 'delete_table':
            Manager.delete_existing_table(database)
        elif manager_input == 'show_menu':
            show_menu(database)
        elif manager_input == 'show_table':
            show_table(database)
        elif manager_input == 'exit':
            print("~~~~~~~~~~~Bye Manager!~~~~~~~~~~~")
            print()
            break
        else:
            print("Invalid input.")
        print()
        input("Enter to continue.....")
        print()

def employee_page(database):
    while True:
        print("================================================================")
        print("================================================================")
        print("Welcome team")
        print("================================================================")
        print("================================================================")
        print()
        print("~~~~~~~~~~~ Reservation ~~~~~~~~~~~~~~~~~~~~~~~")
        print("Display all bookings [type 'get_bookings'].")
        print("Create a new booking [type 'new_booking'].")
        print("Edit an existing booking [type 'edit_booking'].")
        print("Delete an existing booking [type 'delete_booking'].")
        print()
        print("~~~~~~~~~~~ Order ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("TBA")
        print("Create order payment [type 'pay']")
        print()
        print("~~~~~~~~~~~ Table ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Display all tables [type 'show_table'].")
        print("Assign Customer to Table [type 'assign_table']")
        print("Clean Table [type 'clean_table']")
        print()
        print("~~~~~~~~~~~ Exit ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Exit [type 'exit'].")
        print()
        employee_input = input("Select an action: ")
        print()
        if employee_input == 'get_bookings':
            Booking.show_bookings(database.get_bookings())
        elif employee_input == 'new_booking':
            WaitStaff.create_booking(database)
        elif employee_input == 'edit_booking':
            WaitStaff.edit_booking(database)
        elif employee_input == 'delete_booking':
            WaitStaff.delete_booking(database)
        elif employee_input == 'pay':
            payment_handling(database)
        elif employee_input == 'show_table':
            show_table(database)
        elif employee_input == 'assign_table':
            WaitStaff.assign_customer_to_table(database)
        elif employee_input == 'clean_table':
            WaitStaff.clean_table(database)
        elif employee_input == 'exit':
            print("Bye Team!")
            print()
            break
        else:
            print("Invalid input.")
        print()
        input("Enter to continue.....")
        print()

def show_login(database):
    print("Login Page: ")
    print()
    username = input("Enter username: ")
    password = input("Enter password: ")
    print()

    if username == "manager" and password == "manager_password":
        manager_page(database)
    elif username == "wait" and password == "wait_password":
        employee_page(database)
    elif username == "kitchen" and password == "kitchen_password":
        print("TBA")
    else:
        print("Wrong credentials.")
    print()
    input("Enter to continue.....")
    print()

def main(database):
    print("================================================================")
    print("================================================================")
    print("Welcome to Cosy Kangaroo!")
    print()
    print("Provided is a category of options you can navigate to.")
    print("To navigate through our system, please enter the available keywords included inside []")
    print("================================================================")
    print("================================================================")
    print()
    while True:
        print("Choose an action: ")
        print()
        print("~~~~~~~~~~~ Current Menu ~~~~~~~~~~~~~~~~~~~")
        print("Display menu [type 'menu'].")
        print()
        print("~~~~~~~~~~~ Create a Reservation ~~~~~~~~~~~")
        print("Create New Reservation [type 'booking']")
        print()
        print("~~~~~~~~~~~ Log In ~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Log In [type 'login']")
        print()
        print("~~~~~~~~~~~ Exit ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Exit [type 'exit'].")
        print()
        # response to action
        print("================================================================")
        welcome_page_input = input("Enter action: ")
        print()
        if welcome_page_input == "menu":
            print("================================================================")
            show_menu(database)
        elif welcome_page_input == "booking":
            print("================================================================")
            User.create_booking(database)
        elif welcome_page_input == "login":
            print("================================================================")
            show_login(database)
        elif welcome_page_input == 'exit':
            print("Bye")
            break
        else:
            print("Invalid input.")
        print()
        input("Enter to continue.....")
        print("================================================================")
        print()

if __name__ == "__main__":
    # reference to access the databases
    database = Database()
    main(database)