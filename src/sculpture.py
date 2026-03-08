class Sculpture:
    def __init__(self, name : str, artist: str, material: str):
        self.name = name
        self.artist = artist
        self.material = material

    def __str__(self):
        return f"{self.name} by {self.artist}"

    def get_art_type(self):
        return "Sculpture"

    def get_details(self):
        return f"Type: {self.get_art_type()} | Artist: {self.artist} | Material: {self.material}"
    
    def get_material(self):
        return self.material
    
    def get_artist(self):
        return self.artist

    def get_name(self):
        return self.name
    
    