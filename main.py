from database import Database
from item import Item


def main():
    database = Database()
    # delete current menu
    for item in database.get_menu().items:
        database.delete_menu_item(item.id)

    database.create_menu_item(Item(1, "Test1", 10, ["ingredient1", "ingredient2", "ingredient3"]))
    database.create_menu_item(Item(2, "Test2", 10, ["ingredient1", "ingredient2"]))
    database.create_menu_item(Item(3, "Test3", 10, ["ingredient1", "ingredient2", "ingredient3", "ingredient4"]))

    # database.delete_menu_item()

    database.create_menu_item(
        Item(3, "Testchange3", 90, ["ingredient1", "ingredient2", "ingredient3", "ingredient4", "ingredient5"]))

    database.delete_menu_item(2)

    print(database.get_menu().items)

if __name__ == "__main__":
    main()

