#interface.py

class MainMenu:
    def __init__(self):
        self = self

    def __str__(self):
        print("Class responsible for main menu")

    def print_options(self):
        menu = "Wybierz co chcesz zrobić: \n \
Obejrzyj miejsce, przy który stoisz (/inspect) | \
Przejdź w lewo (/left) lub prawo (/right) | \n\
Weź przedmiot (/take) | \
Użyj przedmiotu z plecaka (/use) | \
Odłóż przedmiot (/throw) \n"
        decision = input(menu)
        return decision


