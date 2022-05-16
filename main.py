from database import Database
from item import Item

def main():
    database = Database()
    print("1")
    database.create_menu_item(Item("Test1", 10, ["ingredient1", "ingredient2", "ingredient3"]))
    print("2")
    database.create_menu_item(Item("Test2", 10, ["ingredient1", "ingredient2", "ingredient3"]))
    print("3")
    database.create_menu_item(Item("Test3", 10, ["ingredient1", "ingredient2", "ingredient3"]))
    print("4")

    #database.delete_menu_item()

    database.delete_menu_item(Item("Test1", 10, ["ingredient1", "ingredient2", "ingredient3"]))

    print(database.get_menu().items)

    

if __name__ == "__main__":
    main()