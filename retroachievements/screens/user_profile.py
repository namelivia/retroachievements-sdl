from retroachievements.widgets.user_info import UserInfo
from retroachievements.widgets.game import Game
import wget


def _get_resource(key):
    cache_dir = "/tmp"
    resources_base_url = "http://retroachievements.org/"
    url = f"{resources_base_url}{key}"
    return wget.download(url, out=cache_dir)


class UserProfile:
    def __init__(self, renderer, data):
        self.renderer = renderer
        self.widgets = [
            UserInfo(
                renderer,
                0,
                0,
                {
                    "Avatar": _get_resource(data["UserPic"]),
                    "Points": data["Points"],
                    "TotalRanked": data["TotalRanked"],
                    "Status": data["Status"],
                    "MemberSince": data["MemberSince"],
                },
            ),
            Game(
                renderer,
                0,
                150,
                {
                    "Icon": _get_resource(data["RecentlyPlayed"][0]["ImageIcon"]),
                    "ConsoleName": data["RecentlyPlayed"][0]["ConsoleName"],
                    "Title": data["RecentlyPlayed"][0]["Title"],
                    "LastPlayed": data["RecentlyPlayed"][0]["LastPlayed"],
                },
            ),
            Game(
                renderer,
                0,
                300,
                {
                    "Icon": _get_resource(data["RecentlyPlayed"][1]["ImageIcon"]),
                    "ConsoleName": data["RecentlyPlayed"][1]["ConsoleName"],
                    "Title": data["RecentlyPlayed"][1]["Title"],
                    "LastPlayed": data["RecentlyPlayed"][1]["LastPlayed"],
                },
            ),
            Game(
                renderer,
                0,
                450,
                {
                    "Icon": _get_resource(data["RecentlyPlayed"][2]["ImageIcon"]),
                    "ConsoleName": data["RecentlyPlayed"][2]["ConsoleName"],
                    "Title": data["RecentlyPlayed"][2]["Title"],
                    "LastPlayed": data["RecentlyPlayed"][2]["LastPlayed"],
                },
            ),
        ]

    def run(self):
        self.renderer.clear(0)
        [widget.run() for widget in self.widgets]
