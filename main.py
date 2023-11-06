from Classes.player import Player
from Classes.item import Item
from Classes.room import Room
from Classes.location import table, window, cupboard, door, locations_dict
from Classes.interface import MainMenu
from text import intro
import functions as f

while True:
    #player_name = input("Enter name of your character: ")
    player_name = "Filip"
    backpack = []

    player = Player(player_name, backpack)
    main_room = Room("Main room")
    main_menu = MainMenu()

    main_room.__str__(player_name)

    while True:
        choice = main_menu.print_options()
        match choice:
            case "/sprawdź":
                f.inspect(main_room.current_position, main_room, locations_dict)
            case "/lewo":
                main_room.current_position = f.move_left(main_room.current_position)
                print(f"Stoisz teraz przed: {main_room.locations[main_room.current_position]}")
            case "/prawo":
                main_room.current_position = f.move_right(main_room.current_position)
                print(f"Stoisz teraz przed: {main_room.locations[main_room.current_position]}")
            case "/weź":
                f.take_item(main_room.current_position, locations_dict)
            case "/użyj":
                f.use_item()
            case "/wyrzuć":
                f.throw_item()
            case "/zakończ":
                exit()











