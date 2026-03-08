"""
    main.py
    Francisco Javier Ramos Jimenez.
    Date: 06/03/2026
    Activity: Pull Request and Code Review
    Subject: Software Quality
    V 1.0.0
"""

from museum import Museum
from oeuvre import Oeuvre
from sculpture import Sculpture


def __main__():
    museum = Museum("Louvre", "Paris")

    mona_lisa = Oeuvre("Mona Lisa", "Leonardo da Vinci", 1503)
    liberty = Sculpture("Statue of Liberty", "Frederic Auguste Bartholdi", "Copper")

    museum.add_oeuvre(mona_lisa)
    museum.add_sculpture(liberty)

    print(museum)
    print()
    museum.artwork_details()


if __name__ == "__main__":
    __main__()