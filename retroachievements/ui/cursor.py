import sdl2


class Cursor:
    def __init__(self, renderer, x, y, path):
        self.renderer = renderer
        self.x = x
        self.y = y
        self.path = path

    def update(self, tick):
        pass

    def draw(self):
        try:
            factory = sdl2.ext.SpriteFactory(renderer=self.renderer)
            image = factory.from_image(self.path)
            self.renderer.copy(
                image, dstrect=(self.x, self.y, image.size[0], image.size[1])
            )
        except Exception as e:
            print(str(e))
            exit()
