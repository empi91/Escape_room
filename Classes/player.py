#player.py
class Player:
    def __init__(self, name, backpack):
        self.name = name
        self.backpack = backpack

    def __str__(self):
        return f"{self.name} is your character"

    def take_item(self):
        print(f"You took: {self.name}")

    def throw_item(self, item_name):
        print(f"You thrown: {self.name}")

    def check_backpack(self):
        print(f"Content of the backpack: {self.backpack}")
