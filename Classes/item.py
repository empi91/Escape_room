#item.py

class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print(f"{self.name} description")

    def use_item(self):
        print(f"{self.name} used")