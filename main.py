import pygame

import settings
import settings as st
import sys

class Game():
    def __init__(self):
        pygame.init()

        # Pygame stuff
        self.monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        self.screen = pygame.display.set_mode((st.default_x_size, st.default_y_size), pygame.RESIZABLE)
        pygame.display.set_caption("Arrow Game")

        # timer stuff
        self.clock = pygame.time.Clock()
        self.frame = 0



    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                if not st.fullscreen:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    st.default_x_size = self.screen.get_width()
                    st.default_y_size = self.screen.get_height()

    def check_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_f]:
            self.toggle_fullscreen()
        if keys[pygame.K_PLUS]:
            st.sc_selector += 1
        if keys[pygame.K_MINUS]:
            st.sc_selector -= 1

    def toggle_fullscreen(self):
        if st.fs_is_pressed == False:
            st.fs_start_time = self.frame
            st.fullscreen = not st.fullscreen
            if st.fullscreen:
                self.screen = pygame.display.set_mode(self.monitor_size, pygame.FULLSCREEN)
            else:
                self.screen = pygame.display.set_mode((st.default_x_size, st.default_y_size),
                                                      pygame.RESIZABLE)
        st.fs_is_pressed = True
        if self.frame - st.fs_start_time > st.fs_delay:
            st.fs_is_pressed = False

    def update_screen(self):
        if st.sc_selector == 0:
            self.screen.fill(st.DARK_BLUE)
            print("main menu scene")
        elif st.sc_selector == 1:
            self.screen.fill(st.GREEN)
            print("settings scene")
        elif st.sc_selector == 2:
            self.screen.fill(st.YELLOW)
            print("level selector scene")


        pygame.display.flip()



    def tick(self):
        self.event_handler()
        self.check_keys()
        self.update_screen()

        self.frame += 1
        self.clock.tick(settings.fps)

    def gameplay(self):
        pass
        # TODO Add gameplay


def main():
    game = Game()
    while True:
        game.tick()

main()