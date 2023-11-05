# location.py

class Location:

    def __init__(self, name, items, description):
        self.name = name
        self.items = items
        self.description = description

    def __str__(self):
        return f"{self.description}"


table = Location(
    "stół",
    [],
    "To jest stół"
)

window = Location(
    "okno",
    [],
    "To jest okno"
)

door = Location(
    "drzwi",
    [],
    "To są zamknięte drzwi"
)

cupboard = Location(
    "szafka",
    [],
    "To jest szafka"
)


locations_dict = {
    "stół": table,
    "okno": window,
    "drzwi": door,
    "szafka": cupboard
}
