from table import Table
from item import Item
from wait_staff import WaitStaff
from manager import Manager
from kitchen_staff import KitchenStaff
from timer import Timer

class Order:
    _observers = []
    _states = {1: "Created", 2: "Sent", 3: "Waiting", 4: "Long Wait", 5: "Finished"}

    def __init__(self, table: Table):
        self.table = table
        self.items: list[Item] = []
        self.total = 1
        self.state = self._states[1]
        self.item_index = -1
        self.timer = Timer()

    def __str__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.item_index <= len(self.items) - 2:
            self.item_index += 1
            return self.items[self.item_index]
        else:
            raise StopIteration

    def __len__(self):
        return len(self.items)

    def add_item(self, item: Item):
        self.items.append(item)

    def add_items(self, items: list[Item]):
        self.items += items

    def cancel_item(self, item: Item):
        try:
            self.items.remove(item)
        except ValueError:
            print("Item does not exist")
        else:
            print(str(item) + "successfully deleted from order")

    def send_to_kitchen(self, kitchen: KitchenStaff):
        self._observers.append(kitchen)
        self.timer.start()

    def wait_time(self):
        if self.state:
            return self.timer.elapsed_time()
        else:
            print("Order has been finished")
            return None

    def _notify(self):
        for observer in self._observers:
            observer.update(self.state)

    def finish(self):
        self.state = self._states[4]
        self._notify()
        self._observers.clear()


an_item = Item(1, "betel", 12, "abc")
a_table = Table(4)
an_order = Order(a_table)
for i in range(10):
    an_order.add_item(an_item)
for item in an_order:
    print(item)
