#location.py

class Location:
    items = []
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print(f"{self.name} description")