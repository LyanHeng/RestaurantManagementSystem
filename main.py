from database import Database
from booking import Booking
from employee import Employee
from kitchen_staff import KitchenStaff
from manager import Manager
from table import Table
from payment import Payment
from menu import Menu
from card_payment import CardPayment
from cash_payment import CashPayment
from wait_staff import WaitStaff
from order import Order


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


def show_bookings(database):
    print("Current Bookings: ")
    print()
    id = 'Id'.ljust(5)
    name = 'Name'.ljust(25)
    time = 'Time'.ljust(10)
    table = 'Table'.ljust(7)
    print('{0}{1}{2}{3}'.format(id, name, time, table))
    bookings = database.get_bookings()
    for booking in bookings:
        id = str(getattr(booking, 'id')).ljust(5)
        name = str(getattr(booking, 'name')).ljust(25)
        time = str(getattr(booking, 'time')).ljust(10)
        table = str(getattr(booking, 'table')).ljust(7)
        print('{0}{1}{2}{3}'.format(id, name, time, table))


def booking_handling(database):
    print("Add New Booking: ")
    print()
    name = input("Enter name: ")
    time = input("Enter time of booking: ")
    database.create_booking(
        Booking(database.generate_id(database.BOOKINGS_FILE), name, time, 0))
    print("Your booking has been created!")


def order_handling(database):
    print("Current Orders: ")
    print()
    id = 'ID'.ljust(5)
    table = 'Table'.ljust(10)
    items = 'Item'.ljust(25)
    state = 'State'.ljust(10)
    print('{0}{1}{2}{3}'.format(id, table, items, state))
    orders = database.get_orders()
    for order in orders:
        id = str(order.id).ljust(5)
        table_id = str(order.table.id).ljust(10)
        items = ''
        for item in order.items:
            items += item.name + ', '
        items = str(items[:-2]).ljust(25)
        state = str(order.state).ljust(10)
        print('{0}{1}{2}{3}'.format(id, table_id, items, state))


def add_order(database):
    print("Add New Order: ")
    print()
    show_table(database)
    table_number = input("Enter table number: ")
    order_item = []
    current_item = ''
    while current_item != 'done':
        show_menu(database)
        current_item = input("Enter item number: ")
        if current_item == 'done':
            break
        elif not current_item.isnumeric():
            print("Not valid")
            continue
        elif database.get_item(current_item):
            order_item.append(int(current_item))
    if len(order_item) > 0:
        WaitStaff.create_order(database, order_item, table_number)
        print("Order Created!")
    else:
        print("Order Creation Issue.")


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
                break
            else:
                print("Please enter card/cash/exit")
                continue
            payment.state = payment.process_payment()
            # print invoice if success, offers retry if failed
            if payment.state == "Success":
                payment.print_invoice(True) if type(
                    payment) == CashPayment else payment.print_invoice(False)
            print(payment.state)
            print()
            input("Enter to continue.....")
            print()
    if payment.state == "Failed" or amount_due == -1:
        print("Payment exited")
    else:
        print("Payment completed!")
        # close order
        WaitStaff.clean_table(database, payment.order)
        print("Table " + str(payment.order.table.id) + " now freed")


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
            show_menu(database)
            Manager.delete_item(database)
        elif manager_input == 'new_table':
            Manager.create_new_table(database)
        elif manager_input == 'edit_table':
            Manager.edit_existing_table(database)
        elif manager_input == 'delete_table':
            show_table(database)
            Manager.delete_existing_table(database)
        elif manager_input == 'show_menu':
            show_menu(database)
        elif manager_input == 'show_table':
            show_table(database)
        elif manager_input == 'exit':
            print("Bye Manager!")
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
        print("Displaying all orders [type 'get_orders']")
        print("Create new order [type 'new_order']")
        print("Edit an existing order [type 'edit_order']")
        print("Delete an order [type 'delete_order']")
        print("Delivered order [type 'delivered_order']")
        print("Create order payment [type 'pay']")
        print()
        print("~~~~~~~~~~~ Table ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Display all tables [type 'get_tables'].")
        print("Assign Customer to Table [type 'assign_table']")
        print()
        print("~~~~~~~~~~~ Exit ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Exit [type 'exit'].")
        print()
        employee_input = input("Select an action: ")
        print()
        if employee_input == 'get_bookings':
            show_bookings(database)
        elif employee_input == 'new_booking':
            WaitStaff.create_booking(database)
        elif employee_input == 'edit_booking':
            print("TBA")
        elif employee_input == 'delete_booking':
            print("TBA")
        elif employee_input == 'get_orders':
            order_handling(database)
        elif employee_input == 'edit_order':
            print("Edit Order: ")
            print()
            WaitStaff.modify_order(database)
        elif employee_input == 'delete_order':
            print("Delete Order: ")
            print()
            WaitStaff.delete_order(database)
        elif employee_input == 'new_order':
            add_order(database)
        elif employee_input == 'delivered_order':
            print("Changing Order Status: ")
            print()
            WaitStaff.deliver_item(database)
        elif employee_input == 'pay':
            payment_handling(database)
        elif employee_input == 'get_tables':
            show_table(database)
        elif employee_input == 'assign_table':
            WaitStaff.assign_customer_to_table(database)
        elif employee_input == 'exit':
            print("Bye Team!")
            print()
            break
        else:
            print("Invalid input.")
        print()
        input("Enter to continue.....")
        print()
        

def kitchen_page(database):
    while True:
        print("================================================================")
        print("================================================================")
        print("Welcome kitchen team")
        print("================================================================")
        print("================================================================")
        print()
        print("~~~~~~~~~~~ Order ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Displaying all orders [type 'get_orders']")
        print("Start order [type 'start_order']")
        print("Send order [type 'send_order']")
        print()
        print("~~~~~~~~~~~ Exit ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Exit [type 'exit'].")
        print()
        employee_input = input("Select an action: ")
        print()
        if employee_input == 'get_orders':
            order_handling(database)
        elif employee_input == 'start_order':
            print("Starting Order: ")
            print()
            order_handling(database)
            KitchenStaff.start_order(database)
        elif employee_input == 'send_order':
            print("Completed Order: ")
            print()
            KitchenStaff.completed_order(database)    
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
        kitchen_page(database)
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
            booking_handling(database)
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
