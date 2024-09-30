from settings import *
import pygame



class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        #set up
        super().__init__(groups)
        #importing images for frames
        self.load_images()
        self.state, self.frame_index = "down", 0
        self.image = pygame.image.load(join("..","images","player","down","0.png")).convert_alpha()
        self.rect = self.image.get_frect(center=(pos))
        self.hitbox_rect = self.rect.inflate(-60, -90)

        #speed
        self.direction = pygame.Vector2()
        self.speed = 500
        self.collision_sprites = collision_sprites

    def load_images(self):
        self.frames = {"left": [], "right": [], "up": [], "down": []}
        
        
        for state in self.frames.keys():
            for folder_path, sub_folders, file_names in walk(join("..","images","player", state)):
                #To make sure the file name are loaded in order
                if file_names:
                    for file_name  in sorted(file_names, key= lambda name : int(name.split(".")[0])):
                        full_path = join(folder_path, file_name)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)



    def input(self):
        #return a list of boolean that returns true of the key is pressed at the index of list
        keys = pygame.key.get_pressed()
        #if returns true for Right then 1-0, else 0-1 for left.
        self.direction.x = int(keys[pygame.K_d] - int(keys[pygame.K_a]))
        self.direction.y = int(keys[pygame.K_s] - int(keys[pygame.K_w]))
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        #left side of rect
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        #checking collision on x axis
        self.collision("horizontal")
        #top side of rect
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision("vertical")

        self.rect.center = self.hitbox_rect.center


    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                if direction == "horizontal":
                    #if colliding and moving right, set the coordinate of left to right of the colliding object
                    if self.direction.x > 0: self.hitbox_rect.right = sprite.rect.left
                    #vice versa
                    if self.direction.x < 0: self.hitbox_rect.left = sprite.rect.right
                else:
                    #moving up
                    if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom
                    #moving down
                    if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top

    def animate(self, dt):
        #get state


        #animate
        self.frame_index += 5 * dt
        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)