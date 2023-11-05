#room.py
class Room:
    current_position = 0

    def __init__(self, name, locations):
        self.name = name
        self.locations = locations

    def __str__(self):
        print(f"{self.name} description")

    def move_left(self):
        return self.current_position

    def move_right(self):
        return self.current_position