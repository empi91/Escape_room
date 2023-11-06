# player.py
class Player:
    def __init__(self, name, backpack):
        self.name = name
        self.backpack = backpack

    def __str__(self):
        return f"{self.name} is your character"
