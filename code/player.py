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
        #checking collision on x axis
        self.collision("horizontal")
        #top side of rect
        self.rect.y += self.direction.y * self.speed * dt
        self.collision("vertical")


    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == "horizontal":
                    #if colliding and moving right, set the coordinate of left to right of the colliding object
                    if self.direction.x > 0: self.rect.right = sprite.rect.left
                    #vice versa
                    if self.direction.x < 0: self.rect.left = sprite.rect.right
                else:
                    #moving up
                    if self.direction.y < 0: self.rect.top = sprite.rect.bottom
                    #moving down
                    if self.direction.y > 0: self.rect.bottom = sprite.rect.top

    def update(self, dt):
        self.input()
        self.move(dt)