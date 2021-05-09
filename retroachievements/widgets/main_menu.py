import os
from retroachievements.ui.text import Text
from retroachievements.ui.cursor import Cursor


class MainMenu:
    def __init__(self, renderer, x, y):
        self.renderer = renderer
        self.selected_option = 3
        self.elements = [
            Cursor(
                self.renderer,
                x + 10,
                self._place_cursor(self.selected_option) + 10,
                os.path.dirname(os.path.realpath(__file__))
                + "/../../resources/cursor.png",
            ),
            Text(self.renderer, x + 100, y + 10, "1 - User Profile"),
            Text(self.renderer, x + 100, y + 110, "2 - Other Option"),
            Text(self.renderer, x + 100, y + 210, "3 - Another Option"),
            Text(self.renderer, x + 100, y + 310, "4 - And Yet Another Option"),
        ]

    def _place_cursor(self, selected_option):
        return {
            1: 10,
            2: 110,
            3: 210,
            4: 310,
        }[selected_option]

    def run(self, tick):
        [element.update(tick) for element in self.elements]
        [element.draw() for element in self.elements]
