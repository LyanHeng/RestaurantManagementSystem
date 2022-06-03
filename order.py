from table import Table
from item import Item
from timer import Timer


class Order:
    _states = {1: "Created",
               2: "Started Cooking", 3: "Finished Cooking", 4: "Delivered", 5: "Finished"}

    def __init__(self, id, table: Table):
        self.id = id
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

    def add_items(self, items):
        self.items += items

    def cancel_item(self, item: Item):
        try:
            self.items.remove(item)
        except ValueError:
            print("Item does not exist")
        else:
            print(str(item) + "successfully deleted from order")

    def wait_time(self):
        if self.state:
            return self.timer.elapsed_time()
        else:
            print("Order has been finished")
            return None
            
    def change_state(self, database, state_num):
        if self.state == self._states[state_num - 1]:
            self.state = self._states[state_num]
            database.edit_order(int(self.id), item_ids=None, table_id=None, state=self.state)
        else:
            print("Cannot perform such state change")
