import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, image=None, width=50, height=50, color="white"):
        super().__init__()
        if image is not None:
            self.image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.image, [width, height])
        else:
            self.image = pygame.Surface([width, height])
            self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)


class Block(Object):
    def __init__(self, x: int, y: int, block_id: int, image=None):
        super().__init__(x, y, image)
        self.block_id = block_id