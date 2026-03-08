class Oeuvre:
    def __init__(self, name : str, author : str, year : int):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.name} by {self.author} ({self.year})"

    def get_art_type(self):
        return "Oeuvre"

    def get_details(self):
        return f"Type: {self.get_art_type()} | Author: {self.author} | Year: {self.year}"
    
    def get_year(self):
        return self.year
    
    def get_author(self):
        return self.author
    
    def get_name(self):
        return self.name

    