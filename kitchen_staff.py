from employee import Employee
from order import Order


class KitchenStaff(Employee):
    def __init__(self, name):
        super().__init__(name)

    def get_order(self, order: Order):
        pass

    def item_complete(self):
        pass

    def order_complete(self, order: Order):
        pass

    def update(self, order_state: String):
        print(order_state)



    