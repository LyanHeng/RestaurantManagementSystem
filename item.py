import string


class Item:
    def __init__(self, item_id, name: string, price, ingredients):
        self.id = item_id
        self.price = price
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return self.name
