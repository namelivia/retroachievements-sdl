import os
import sdl2.ext
from retroachievements.client import RetroAchievementsWebApiClient

# from retroachievements.screens.user_profile import UserProfile
from retroachievements.screens.main_menu import MainMenu


if __name__ == "__main__":
    client = RetroAchievementsWebApiClient(
        os.environ["RETROACHIEVEMENTS_USERNAME"],
        os.environ["RETROACHIEVEMENTS_KEY"],
    )
    data = client.GetUserSummary("namelivia", 3)
    print(data)
    sdl2.ext.init()
    window = sdl2.ext.Window(
        "RetroAchievements", size=(800, 600), flags=sdl2.SDL_WINDOW_SHOWN
    )
    renderer = sdl2.ext.Renderer(window)
    running = True
    screen = MainMenu(renderer, data)
    tick = 0

    while running:
        tick += 1
        screen.run(tick)
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
        renderer.present()
        window.refresh()
