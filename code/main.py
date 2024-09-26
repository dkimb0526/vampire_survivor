from settings import *
import pygame
from os.path import join
from player import Player
from sprites import *
from pytmx.util_pygame import load_pygame
from random import randint, uniform
from groups import AllSprites



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
        #class object from groups.py
        self.all_sprites = AllSprites()
        #used in play class for collision logic
        self.collision_sprites = pygame.sprite.Group()

        self.setup()

        #sprites
        self.player = Player((500,300), self.all_sprites, self.collision_sprites)

    def setup(self):
        #import map objects
        map = load_pygame(join("..","data","maps","world.tmx"))


        for x, y, image in map.get_layer_by_name("Ground").tiles():
            #x and y only for the position, but we need increase for each size of tile
            Sprite((x*TILE_SIZE,y*TILE_SIZE), image, self.all_sprites)
        for obj in map.get_layer_by_name("Objects"):
            CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))
            #print(obj.x)
            #print(obj.y)
            #print(obj.image)
        for obj in map.get_layer_by_name("Collisions"):
            CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)



    def run(self):
        while self.running:
            #only one slash so it could be a float
            dt = self.clock.tick()/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.display_surface.fill("darkgoldenrod1")
            #display surface being called in groups.py
            self.all_sprites.draw(self.player.rect)
            self.all_sprites.update(dt)
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()


