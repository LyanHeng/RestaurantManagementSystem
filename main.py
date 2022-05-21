from database import Database
from item import Item
from table import Table
from booking import Booking
from user import User
import json 

def main():
    database = Database()

    # delete current menu
    for item in database.get_menu().items:
        database.delete_menu_item(item.id)

    database.create_menu_item(Item(database.generate_id(database.ITEMS_FILE), "Test1", 10, ["ingredient1", "ingredient2", "ingredient3"]))
    database.create_menu_item(Item(database.generate_id(database.ITEMS_FILE), "Test2", 10, ["ingredient1", "ingredient2"]))
    database.create_menu_item(Item(database.generate_id(database.ITEMS_FILE), "Test3", 10, ["ingredient1", "ingredient2", "ingredient3", "ingredient4"]))

    database.edit_menu_item(Item(1, "Testchange3", 90, ["ingredient1", "ingredient2", "ingredient3", "ingredient4", "ingredient5"]))

    database.delete_menu_item(2)

    # delete current tables
    for table in database.get_tables():
        database.delete_table(table.id)

    database.create_table(Table(1, 4, "free"))
    database.create_table(Table(2, 4, "free"))
    database.create_table(Table(3, 4, "free"))
    database.create_table(Table(4, 4, "free"))

    database.edit_table(Table(4, 6, "free"))

    # delete current booking
    for booking in database.get_bookings():
       database.delete_booking(booking.id)

    database.create_booking(Booking(1, "Bob", 0, 1))
    database.create_booking(Booking(2, "Fred", 0, 1))
    database.create_booking(Booking(3, "Mary", 0, 1))
    database.create_booking(Booking(4, "Jane", 0, 1))

    database.edit_booking(Booking(3, "john", 0, 1))

    print("Create Booking")
    User.create_booking()
    print("Create Booking 2")
    User.create_booking()

    

if __name__ == "__main__":
    main()