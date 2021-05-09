from retroachievements.ui.text import Text
from retroachievements.ui.image import Image


class Game:
    def __init__(self, renderer, x, y, data):
        self.renderer = renderer
        self.elements = [
            Image(self.renderer, x + 10, y + 10, data["Icon"]),
            Text(self.renderer, x + 120, y + 10, "Console: " + data["ConsoleName"]),
            Text(self.renderer, x + 120, y + 30, "Title: " + data["Title"]),
            Text(self.renderer, x + 120, y + 50, "LastPlayed: " + data["LastPlayed"]),
        ]

    def run(self):
        [element.update() for element in self.elements]
        [element.draw() for element in self.elements]
