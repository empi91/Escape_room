# functions.py
from Classes.room import Room


def inspect(current_position, room, location_dict):
    name = room.locations[current_position]
    location = location_dict[name]
    print(location)


def move_left(current_position):
    if current_position > 0:
        current_position = current_position - 1
    else:
        current_position = 3
    return current_position


def move_right(current_position):
    if current_position < 3:
        current_position += 1
    else:
        current_position = 0
    return current_position


def take_item():
    print("You took the item")


def use_item():
    print("You used the item")


def throw_item():
    print("You thrown the item")


