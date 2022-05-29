from database import Database
from booking import Booking
from employee import Employee
from manager import Manager
from table import Table
from payment import Payment
from menu import Menu
from card_payment import CardPayment
from cash_payment import CashPayment
from wait_staff import WaitStaff

def show_menu(database):
    id = 'Id'.ljust(5)
    name = 'Name'.ljust(25)
    price = 'Price'.ljust(10)
    ingredients = 'Ingredients'.ljust(7)
    print('{0}{1}{2}{3}'.format(id, name, price, ingredients))
    Menu.display_item(database.get_menu().items)

def show_table(database):
    id = 'Id'.ljust(5)
    size = 'Size'.ljust(25)
    state = 'State'.ljust(10)
    print('{0}{1}{2}'.format(id, size, state))
    Table.display_table(database.get_tables())

def show_bookings(database):
    id = 'Id'.ljust(5)
    name = 'Name'.ljust(25)
    time = 'Time'.ljust(10)
    table = 'Table'.ljust(7)
    print('{0}{1}{2}{3}'.format(id, name, time, table))
    bookings = database.get_bookings()
    for booking in bookings:
        id = str(getattr(booking,'id')).ljust(5)
        name = str(getattr(booking,'name')).ljust(25)
        time = str(getattr(booking,'time')).ljust(10)
        table = str(getattr(booking,'table')).ljust(7)
        print('{0}{1}{2}{3}'.format(id,name,time,table))
    print()

def booking_handling(database):
    name = input("Enter name: ")
    time = input("Enter time of booking: ")
    database.create_booking(Booking(database.generate_id(database.BOOKINGS_FILE), name, time, 0))
    print("Your booking has been created!")

def payment_handling(database):
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
    # TODO: Edit table state

def manager_page(database):
    while True:
        print("~~~~~~~~~~~Welcome manager.~~~~~~~~~~~")
        print("~~~~~~~~~~~Item~~~~~~~~~~~")
        print("Display menu [type 'show_menu'].")
        print("Create a new item [type 'new_menu'].")
        print("Edit an existing item [type 'edit_menu'].")
        print("Delete an existing item [type 'delete_menu'].")
        print()
        print("~~~~~~~~~~~Table~~~~~~~~~~~")
        print("Display all tables [type 'show_table'].")
        print("Create a new table [type 'new_table'].")
        print("Edit an existing table [type 'edit_table'].")
        print("Delete an existing table [type 'delete_table'].")
        print()
        print("~~~~~~~~~~~Exit~~~~~~~~~~~")
        print("Exit [type 'exit'].")
        print()
        manager_input = input("Select an action: ")
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

def employee_page(database):
    while True:
        print("~~~~~~~~~~~Welcome team.~~~~~~~~~~~")
        print("~~~~~~~~~~~Reservation~~~~~~~~~~~")
        print("Display all bookings [type 'get_bookings'].")
        print("Create a new booking [type 'new_booking'].")
        print("Edit an existing booking [type 'edit_booking'].")
        print("Delete an existing booking [type 'delete_booking'].")
        print()
        print("~~~~~~~~~~~Order~~~~~~~~~~~")
        print("TBA")
        print("Create order payment [type 'pay']")
        print()
        print("~~~~~~~~~~~Table~~~~~~~~~~~")
        print("Display all tables [type 'show_table'].")
        print("Assign Customer to Table [type 'assign_table']")
        print()
        print("~~~~~~~~~~~Exit~~~~~~~~~~~")
        print("Exit [type 'exit'].")
        print()
        employee_input = input("Select an action: ")
        if employee_input == 'get_bookings':
            show_bookings(database)
        elif employee_input == 'new_booking':
            WaitStaff.create_booking(database)
        elif employee_input == 'edit_booking':
            print("TBA")
        elif employee_input == 'delete_booking':
            print("TBA")
        elif employee_input == 'pay':
            payment_handling(database)
        elif employee_input == 'show_table':
            show_table(database)
        elif employee_input == 'assign_table':
            WaitStaff.assign_customer_to_table(database)
        elif employee_input == 'exit':
            print("~~~~~~~~~~~Bye Team!~~~~~~~~~~~")
            print()
            break
        else:
            print("Invalid input.")
        print()

def show_login(database):
    print("~~~~~~~~~~~Login Page~~~~~~~~~~~")
    print()
    username = input("Enter username: ")
    password = input("Enter password: ")
    print()

    if username == "manager" and password == "manager_password":
        manager_page(database)
    elif username == "employee" and password == "employee_password":
        employee_page(database)
    else:
        print("Wrong credentials.")

def main(database):
    print("Welcome to Cosy Kangaroo!")
    print()
    print("Provided is a category of options you can navigate to.")
    print("To navigate through our system, please enter the available keywords included inside []")
    print()
    while True:
        print("~~~~~~~~~~~Current Menu~~~~~~~~~~~")
        print("Display menu [type 'menu'].")
        print()
        print("~~~~~~~~~~~Create a Reservation~~~~~~~~~~~")
        print("Create New Reservation [type 'booking']")
        print()
        print("~~~~~~~~~~~Log In~~~~~~~~~~~")
        print("Log In [type 'login']")
        print()
        print("~~~~~~~~~~~Exit~~~~~~~~~~~")
        print("Exit [type 'exit'].")
        print()
        # response to action
        welcome_page_input = input("Enter action: ")
        print()
        if welcome_page_input == "menu":
            show_menu(database)
        elif welcome_page_input == "booking":
            booking_handling(database)
        elif welcome_page_input == "login":
            show_login(database)
        elif welcome_page_input == 'exit':
            print("~~~~~~~~~~~Bye~~~~~~~~~~~")
            print()
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    # reference to access the databases
    database = Database()
    main(database)