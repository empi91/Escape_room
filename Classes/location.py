# location.py
from Classes.item import Item
from text import door_desc, table_desc, cupboard_desc, window_desc


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
        "kod": [True, False],
        "sejf": [False, True]
    },
    table_desc
)

window = Location(
    "okno",
    {
        "kartka z hasłem": [True, True]
    },
    window_desc
)

door = Location(
    "drzwi",
    {},
    door_desc
)

cupboard = Location(
    "szafka",
    {
        "stary klucz": [True, False],
        "skrzyneczka": [False, False]
    },
    cupboard_desc
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
