# room.py
import text


class Room:
    current_position = 3
    locations = ["stół", "szafka", "okno", "drzwi", ]

    def __init__(self, name):
        self.name = name

    def __str__(self, player_name):
        formatted_text = text.intro.format(player_name=player_name, location0=self.locations[0], location1=self.locations[1], location2=self.locations[2], location3=self.locations[3])
        print(formatted_text)

    def move_left(self):
        return self.current_position

    def move_right(self):
        return self.current_position
