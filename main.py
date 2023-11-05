from Classes.player import Player
from Classes.item import Item
from Classes.room import Room
from Classes.location import Location
from Classes.interface import MainMenu
from text import intro

while True:
    print(intro)
    #player_name = input("Enter name of your character: ")
    player_name = "Filip"
    backpack = []

    player = Player(player_name, backpack)
    main_room = Room("Main room")
    main_menu = MainMenu()

    main_room.__str__(player_name)
    main_menu.print_options()

    # for item in main_room.locations:
    #     item = Location(item, [])
    #     #print(item)
    #     #print(type(item))
    #     print(item.name)








