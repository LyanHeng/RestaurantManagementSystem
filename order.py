from table import Table
from item import Item
from wait_staff import WaitStaff
from manager import Manager


class Order:
    def __init__(self, table: Table):
        self.table = table
        self.items: list[Item] = []
        self.total = 0
        self.finished = False

    def __str__(self):
        pass

    def add_item(self, item: Item):
        self.items.append(item)

    def cancel_item(self, item: Item):
        try:
            self.items.remove(item)
        except ValueError:
            print("Item does not exist")
        else:
            print(str(item) + "successfully deleted from order")

    def send_to_kitchen(self):
        pass

    def notify_long_wait:
        pass

    def finish(self):
        self.finished = True

    def finished(self):
        return self.finished











