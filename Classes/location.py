# location.py
from Classes.item import Item


class Location:

    def __init__(self, name, item_name, description):
        self.name = name
        self.items = [Item(name, attributes[0], attributes[1]) for name, attributes in item_name.items()]
        self.description = description

    def __str__(self):
        item_names = []
        for item in self.items:
            if item.visible:
                item_names.append(item.name)
            else:
                continue
        return f"{self.description} \n {', '.join(item_names)}"


table = Location(
    "stół",
    {
        "klucz": [True, True],
        "kartka": [True, False],
        "zeszyt": [False, True]
    },
    f"Przed tobą stoi duży drewniany stół, na którym leżą: "
)

window = Location(
    "okno",
    {},
    "To jest okno"
)

door = Location(
    "drzwi",
    {},
    "To są zamknięte drzwi"
)

cupboard = Location(
    "szafka",
    {},
    "To jest szafka"
)


locations_dict = {
    "stół": table,
    "szafka": cupboard,
    "okno": window,
    "drzwi": door,
}


def get_location_name(current_position):
    if current_position == 0:
        current_location = "stół"
    elif current_position == 1:
        current_location = "szafka"
    elif current_position == 2:
        current_location = "okno"
    elif current_position == 3:
        current_location = "drzwi"
    else:
        current_location = ""
    return current_location
