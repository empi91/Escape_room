# room.py
class Room:
    current_position = 0
    locations = ["stół", "okno", "drzwi", "szafka"]

    def __init__(self, name):
        self.name = name

    def __str__(self, player_name):
        return f"Witaj {player_name}, dobrze, że się obudziłeś! \n\
Znajdujesz się pośrodku dużego, zamkniętego pokoju. \n\
Pod sufitem pali się lampa i widzisz, że w pokoju znajduje się: \n\
{self.locations[0]}, {self.locations[1]}, {self.locations[2]} oraz {self.locations[3]} \n\
W tej chwili stoisz przy stole."


    def move_left(self):
        return self.current_position

    def move_right(self):
        return self.current_position