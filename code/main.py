from settings import *
import pygame
from os.path import join
#from random import randint, uniform

#pygame initialization
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
center_screen = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("vampire survivor")


running = True
clock = pygame.time.Clock()

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
#sprite
all_sprites = pygame.sprite.Group()

#imports
player = Player(all_sprites, pygame.image.load(join("..","images","player","down","0.png")).convert_alpha(),center_screen)

while running:
    #only one slash so it could be a float
    dt = clock.tick()/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill("darkgoldenrod1")
    all_sprites.draw(display_surface)
    all_sprites.update(dt)

    pygame.display.update()


pygame.quit()