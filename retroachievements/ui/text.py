import sdl2
import os


class Text:
    def __init__(self, renderer, x, y, contents):
        self.renderer = renderer
        self.x = x
        self.y = y
        self.contents = contents

    def update(self, tick):
        pass

    def draw(self):
        try:
            manager_font = sdl2.ext.FontManager(
                font_path=os.path.dirname(os.path.realpath(__file__))
                + "/../../resources/OpenSans.ttf",
                size=14,
            )
            factory = sdl2.ext.SpriteFactory(renderer=self.renderer)
            text = factory.from_text(self.contents, fontmanager=manager_font)
            self.renderer.copy(
                text, dstrect=(self.x, self.y, text.size[0], text.size[1])
            )
        except Exception as e:
            print(str(e))
            print("libsdl2-ttf-2.0-0 is required")
            exit()
