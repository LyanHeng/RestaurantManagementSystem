from user import User

class Employee(User):
    def __init__(self, id, name):
        self.id = id
        self.name = name
