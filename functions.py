# functions.py
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


def take_item(player_position, locations_dict, player_backapck):
    item_name = input("Który przedmiot chcesz wziąć?\n")
    location = get_location_name(player_position)

    list_of_items = locations_dict[location].items

    for item in list_of_items:
        if item_name == item.name:
            item.take_item(locations_dict[location].items, item_name, player_backapck)
            return

    print("Nie ma takiego przedmiotu")


def use_item(player_position, player_backpack):
    print("You used the item")
    # if item OK and location OK then action1()


def throw_item(player_position, locations_dict, player_backpack):
    item_name = input("Który przedmiot chcesz wyrzucić?\n")
    location = get_location_name(player_position)

    for item in player_backpack:
        if item_name == item.name:
            item.throw_item(locations_dict[location].items, item_name, player_backpack)
            return

    print("Nie ma takiego przedmiotu")


def check_backpack(player_backpack):
    print("Zawartość twojego plecaka:")
    if player_backpack:
        for item in player_backpack:
            print(item.name)
    else:
        print("Plecak jest pusty")
