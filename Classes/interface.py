# interface.py
import text


class MainMenu:
    def __init__(self):
        pass

    def __str__(self):
        return "Class responsible for main menu"

    def print_options(self):
        decision = input(text.menu)
        return decision

    def print_help(self):
        print(text.interface_help)
