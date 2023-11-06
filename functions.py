# functions.py
from Classes.room import Room
from Classes.location import get_location_name


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


def take_item(player_position, locations_dict):
    item_name = input("Który przedmiot chcesz wziąć?\n")
    location = get_location_name(player_position)
    list_of_items = locations_dict[location].items

    for item in list_of_items:
        if item_name == item.name:
            item.use_item()
        else:
            print("Nie ma takiego przedmiotu")


def use_item():
    print("You used the item")


def throw_item():
    print("You thrown the item")


