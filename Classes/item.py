# item.py
from scritps import check_use


class Item:
    def __init__(self, name, can_be_taken, visible):
        self.name = name
        self.can_be_taken = can_be_taken
        self.visible = visible

    def __str__(self):
        return f"{self.name}"

    def use_item(self, location, used_item, backpack):
        if check_use(location.name, used_item):
            for item in backpack:
                if used_item == item.name:
                    backpack.remove(item)
        else:
            print(f"Nie możesz użyć {used_item} w tym miejscu")

    def take_item(self, list_of_items, taken_item, backpack):
        for item in list_of_items:
            if taken_item == item.name:
                list_of_items.remove(item)
                backpack.append(item)

    def throw_item(self, list_of_items, thrown_item, backpack):
        for item in backpack:
            if thrown_item == item.name:
                backpack.remove(item)
                list_of_items.append(item)
