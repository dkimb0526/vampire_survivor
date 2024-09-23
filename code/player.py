from settings import *
import pygame



class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join("..","images","player","down","0.png")).convert_alpha()
        self.rect = self.image.get_frect(center=(pos))

        #speed
        self.direction = pygame.Vector2()
        self.speed = 500
        self.collision_sprites = collision_sprites

    def input(self):
        #return a list of boolean that returns true of the key is pressed at the index of list
        keys = pygame.key.get_pressed()
        #if returns true for Right then 1-0, else 0-1 for left.
        self.direction.x = int(keys[pygame.K_d] - int(keys[pygame.K_a]))
        self.direction.y = int(keys[pygame.K_s] - int(keys[pygame.K_w]))
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        #left side of rect
        self.rect.x += self.direction.x * self.speed * dt
        #top side of rect
        self.rect.y += self.direction.y * self.speed * dt


    def collision(self, direction):
        pass


    def update(self, dt):
        self.input()
        self.move(dt)