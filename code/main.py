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
                    running = False

            self.display_surface.fill("darkgoldenrod1")
            all_sprites.draw(self.display_surface)
            all_sprites.update(dt)

            pygame.display.update()


        pygame.quit()



class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image, pos):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect(center=(pos))
        self.direction = pygame.Vector2()
        self.speed = 300

    def update(self, dt):
        #return a list of boolean that returns true of the key is pressed at the index of list
        keys = pygame.key.get_pressed()
        #if returns true for Right then 1-0, else 0-1 for left.
        self.direction.x = int(keys[pygame.K_d] - int(keys[pygame.K_a]))
        self.direction.y = int(keys[pygame.K_s] - int(keys[pygame.K_w]))
        self.rect.center += self.direction * self.speed * dt

all_sprites = pygame.sprite.Group()


if __name__ == "__main__":
    game = Game()
    game.run()
#sprite

#imports
player = Player(all_sprites, pygame.image.load(join("..","images","player","down","0.png")).convert_alpha(),
                (WINDOW_WIDTH//2, WINDOW_HEIGHT//2))

