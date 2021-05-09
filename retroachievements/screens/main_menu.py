from retroachievements.widgets.main_menu import MainMenu as MainMenuWidget


class MainMenu:
    def __init__(self, renderer, data):
        self.renderer = renderer
        self.menu_widget = MainMenuWidget(renderer, 0, 0)
        self.widgets = [self.menu_widget]

    def run(self, tick):
        self.renderer.clear(0)
        [widget.run(tick) for widget in self.widgets]
