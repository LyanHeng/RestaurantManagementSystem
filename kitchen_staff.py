from employee import Employee
from order import Order

class KitchenStaff(Employee):
    def start_order(database):
        order_number = input("Enter order number: ")
        if order_number.isnumeric():
            order = database.get_order(order_number)
            order.change_state(database, 2)

    def completed_order(database):
        order_number = input("Enter order number: ")
        if order_number.isnumeric():
            order = database.get_order(order_number)
            order.change_state(database, 3)

    def update(self, order_state):
        print(order_state)