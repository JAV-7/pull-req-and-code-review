from oeuvre import Oeuvre
from sculpture import Sculpture

class Museum:
    def __init__(self, name : str, location : str):
        self.name = name
        self.location = location
        self.oeuvres = []
        self.sculptures = []

    def __str__(self):
        lines = [f"{self.name} is located in {self.location} ",
                 f"has {len(self.oeuvres)} oeuvres and ",
                 f"{len(self.sculptures)} sculptures."]
        return ''.join(lines)
    
    def oeuvres_details(self):
        print("OEUVRES:")
        for oeuvre in self.oeuvres:
            print(f"- {oeuvre.get_details()}")

    def sculptures_details(self):
        print("SCULPTURES:")
        for sculpture in self.sculptures:
            print(f"- {sculpture.get_details()}")

    def artwork_details(self):
        self.oeuvres_details()
        self.sculptures_details()

    def add_oeuvre(self, oeuvre : Oeuvre):
        self.oeuvres.append(oeuvre)

    def add_sculpture(self, sculpture : Sculpture):
        self.sculptures.append(sculpture)

    def remove_oeuvre(self, oeuvre : Oeuvre):
        self.oeuvres.remove(oeuvre)
    
    def remove_sculpture(self, sculpture : Sculpture):
        self.sculptures.remove(sculpture)

    