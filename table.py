from typing import List
from database import Database


class Table:
    states = ["Activated", "Ordered", "Paid"]

    def __init__(self, size):
        self.size = size
        self.state = Table.states[0]

    def update_state(self, state):
        self.state = Table.states[state]
