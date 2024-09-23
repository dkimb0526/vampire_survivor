from settings import *
import pygame
from os.path import join
from player import Player
from sprites import *
from random import randint, uniform


#pygame initialization
class Game:
    def __init__(self):
        #setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("vampire survivor")
        self.running = True
        self.clock = pygame.time.Clock()

        #groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        #sprites
        self.player = Player((400,300), self.all_sprites, self.collision_sprites)
        for i in range(6):
            x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
            w, h = randint(60,100), randint(50,100)
            CollisionSprite((x,y), (w,h), (self.all_sprites, self.collision_sprites))


    def run(self):
        while self.running:
            #only one slash so it could be a float
            dt = self.clock.tick()/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.display_surface.fill("darkgoldenrod1")
            self.all_sprites.draw(self.display_surface)
            self.all_sprites.update(dt)
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()


