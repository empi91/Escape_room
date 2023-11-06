# item.py

class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def use_item(self):
        print(f"{self.name} used")

    def take_item(self, list_of_items, taken_item, backpack):
        for item in list_of_items:
            if taken_item == item.name:
                list_of_items.remove(item)
                backpack.append(item)

    def throw_item(self):
        print(f"{self.name} thrown")