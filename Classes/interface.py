# interface.py

class MainMenu:
    def __init__(self):
        self = self

    def __str__(self):
        return f"Class responsible for main menu"

    def print_options(self):
        menu = "Wybierz co chcesz zrobić: \n \
Obejrzyj miejsce, przy który stoisz (/sprawdź) | \
Przejdź w lewo (/lewo) lub prawo (/prawo) | \n\
Weź przedmiot (/weź) | \
Użyj przedmiotu z plecaka (/użyj) | \
Odłóż przedmiot (/wyrzuć) | \
Wyjdź z gry (/zakończ) \n"
        decision = input(menu)
        return decision


