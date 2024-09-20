from settings import *
import pygame
from os.path import join
#from random import randint, uniform

#pygame initialization
class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("vampire survivor")
        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            #only one slash so it could be a float
            dt = self.clock.tick()/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.display_surface.fill("darkgoldenrod1")
            #all_sprites.draw(self.display_surface)
            #all_sprites.update(dt)
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()


