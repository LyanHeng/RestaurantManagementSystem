from user import User


class Employee(User):
    def __init__(self, name, PIN=0000):
        super().__init__(name)
        self.PIN = PIN
