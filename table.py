from database import Database

class Table():
    def __init__(self, id, size, state):
        self.id = id
        self.size = size
        self.state = state

    def create_new_table(self):
        database = Database()

        size = input("Enter table size: ")
        state = input("Enter table state [free/occupied]: ")

        table = Table(database.generate_id(database.TABLES_FILE), size, state)
        database.create_table(table)

    def edit_table(self):
        id = input("Enter table id: ")   
        #table does not exist in database
        table = Database.get_tables(id)
        if not table:
            print("Table does not exist")
            return -1
            
        table.size = input("Enter table new name: ")
        table.state = input("Enter table new state: ")

        Database.edit_table(table)

    def delete_table(self):
        id = input("Enter table id: ")  
        #table does not exist in database
        table = Database.get_tables(id)
        if not table:
            print("Table does not exist")
            return -1
        Database.delete_table(table)

    def set_table_state(self):
        id = input("Enter table id: ")  
        #table does not exist in database
        table = Database.get_tables(id)
        if not table:
            print("Table does not exist")
            return -1
        table.state = input("Enter table state [free/occupied]: ") 