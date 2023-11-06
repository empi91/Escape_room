# interface.py
import text


class MainMenu:
    def __init__(self):
        self = self

    def __str__(self):
        return f"Class responsible for main menu"

    def print_options(self):
        decision = input(text.menu)
        return decision


