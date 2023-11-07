# scripts.py
import text
import Classes.location

def check_use(location, item):
    match location:
        case 'stół':
            if item == "kartka z hasłem":
                scenario_2()
                return True
            else:
                return False
        case 'drzwi':
            if item == "stary klucz":
                scenario_4()
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
            elif item == "kod":
                scenario_3()
                return True
            else:
                return False
        case _:
            return False


def scenario_1():
    print(text.scenario_1_text)
    # for item in Classes.location.cupboard.items:
    #     if item.name == "skrzyneczka":
    #         item.visible = False
    text.cupboard_desc = text.cupboard_desc_2


def scenario_2():
    print(text.scenario_2_text)
    for item in Classes.location.table.items:
        if item.name == "kod":
            item.visible = True


def scenario_3():
    print(text.scenario_3_text)
    for item in Classes.location.cupboard.items:
        if item.name == "stary klucz":
            item.visible = True
    text.cupboard_desc = text.cupboard_desc_3


def scenario_4():
    print(text.scenario_4_text)
    exit()

