from employee import Employee
from database import Database

class WaitStaff(Employee):
    def assign_customer_to_table():
        pass

    def create_order():
        pass

    def modify_order():
        pass

    def delete_order():
        pass

    def deliver_item():
        pass

    def clean_table():
        pass

    def set_table_state(self):
        id = input("Enter table id: ")  
        #table does not exist in database
        table = Database.get_tables(id)
        if not table:
            print("Table does not exist")
            return -1
        table.state = input("Enter table state [free/occupied]: ") 
    