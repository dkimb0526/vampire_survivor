from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.Vector2()

    def draw(self, target_pos):
        #centering horizontal camera
        #when i move, the center of my char changes so the camera moves with it
        self.offset.x = -(target_pos[0]-WINDOW_WIDTH//2)
        self.offset.y = -(target_pos[1]-WINDOW_HEIGHT//2)

        ground_sprites = [sprite for sprite in self if hasattr(sprite, "ground")]
        object_sprites = [sprite for sprite in self if not hasattr(sprite, "ground")]

        #iterating through the two groups, ground sprite first, then object
        for layer in [ground_sprites, object_sprites]:
        #lambda extracts the y position, then the sorting function sorts based on the y
            for sprite in sorted(layer, key = lambda sprite: sprite.rect.centery):
                self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)