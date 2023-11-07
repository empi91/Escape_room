# scripts.py
import text
from Classes.location import cupboard

def check_use(location, item):
    match location:
        case 'stół':
            print("1")
        case 'drzwi':
            if item == "stary klucz":
                scenario_3()
                return True
            elif item == "klucz":
                print("Chyba nie myślałeś, że to będzie takie proste??")
                return False
            else:
                return False
        case 'szafka':
            if item == "klucz":
                scenario_1()
                return True

        case 'okno':
            print("4")
        case _:
            return False


def scenario_1():
    print(text.scenario_1_text)
    for item in cupboard:
        if item.name == "skrzyneczka":
            item.visible = True


def scenario_2():
    print("")


def scenario_3():
    print(text.scenario_3_text)
    exit()

