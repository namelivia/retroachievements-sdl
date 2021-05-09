from retroachievements.ui.text import Text
from retroachievements.ui.image import Image


class UserInfo:
    def __init__(self, renderer, x, y, data):
        self.renderer = renderer
        self.elements = [
            Image(self.renderer, x + 10, y + 10, data["Avatar"]),
            Text(self.renderer, x + 150, y + 10, "Points: " + data["Points"]),
            Text(self.renderer, x + 150, y + 30, "Rank: " + data["TotalRanked"]),
            Text(self.renderer, x + 150, y + 50, "Status: " + data["Status"]),
            Text(
                self.renderer, x + 150, y + 70, "Member since: " + data["MemberSince"]
            ),
        ]

    def run(self, tick):
        [element.update(tick) for element in self.elements]
        [element.draw() for element in self.elements]
