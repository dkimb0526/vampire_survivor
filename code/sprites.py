from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        #anything from TILES editor use topleft
        self.rect = self.image.get_frect(topleft=pos)
        self.ground= True

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        #anything from TILES editor use topleft
        self.rect = self.image.get_frect(topleft=(pos))