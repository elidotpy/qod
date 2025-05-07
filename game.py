level = """
00000000200000000000000000000000000000000200000000000000000000000000022222222122221222122
00000000200000000000000000000000000000000200000000000000000000000000022222222211111111000
00000000200000000000000000000000000000000000000000000000000000000000000000000000001000000
00000000000000000000000000000000000000000000000000000000000000000000000000010000001222222
00000000000000000000000000000000000000000000111000000000000000000000000002220000001000000
00000000000001000000000200000000000220000222222200000000000000000000000020000000012000000
00000000222222000222200001000010000002222222222222000000000000000002000220000222222000000
00000222222222220111111222222222222111111222222221222000110001100011100100222211111000000
""".strip().splitlines()

def port():
    level_list = []
    start = [0, 50]
    for line in level:
        start[0] = 0
        for objecta in line:
            start[0] += 50
            if objecta != "0" or objecta != 0:
                level_list.append(
                    (int(objecta), start[0], start[1])
                )
        start[1] += 50
    return level_list

import pygame

# initiating
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.init()

speed = 7

# setting window up
proportions = 800, 600
window = pygame.display.set_mode(proportions)

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width=30, height=30):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.speedy = 0
        self.size = (size, size)

        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args, **kwargs):
        self.rect.y += self.speedy

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image = None):
        super().__init__()
        if image is not None:
            self.image = pygame.image.load(image)
            self.image = pygame.transform.scale(self.image, (width, height))
        else:
            self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.killable = False
        self.standable = False

class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y, width=30, height=30):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.killable = True
        self.standable = False

        self.image = pygame.image.load("assets/blocks/1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)

    def update(self, *args, **kwargs):
        self.rect.x -= speed

class Classic(Block):
    def __init__(self, x, y):
        super().__init__(x,y, 50, 50, "assets/blocks/2.png")
        self.image = pygame.image.load("assets/blocks/2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.killable = False
        self.standable = True

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)

    def update(self, *args, **kwargs):
        self.rect.x -= speed

player = Player(50, 400, 50)
floor = Object(0, 450, "white", 800, 500)


all_sprites = pygame.sprite.Group()
objects = pygame.sprite.Group()

all_sprites.add(floor)
all_sprites.add(player)

object_list = {
    "1": Spike,
    "2": Classic
}

level = port()

def parse_level(level):
    objects.empty()
    for data in level:
        if int(data[0]) != 0:
            o = object_list[str(data[0])](data[1], data[2])
            objects.add(o)
            all_sprites.add(o)

parse_level(level)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill("cyan")
    #render here
    keys = pygame.key.get_pressed()

    if player.rect.colliderect(floor.rect):
        player.speedy = floor.rect.y - player.rect.y - player.rect.size[1] + 1
        player.update()
        player.speedy = 0

    if keys[pygame.K_SPACE] and player.rect.colliderect(floor.rect):
        player.speedy = -15

    for object in objects:
        if player.rect.colliderect(object.rect) and object.killable:
            player = Player(50, 400, 50)
            floor = Object(0, 450, "white", 800, 500)

            all_sprites = pygame.sprite.Group()
            objects = pygame.sprite.Group()

            parse_level(level)

            all_sprites.add(floor)
            all_sprites.add(player)
        if player.rect.collidepoint(object.rect.bottomleft) or player.rect.collidepoint(object.rect.bottomright):
            player = Player(50, 400, 50)
            floor = Object(0, 450, "white", 800, 500)

            all_sprites = pygame.sprite.Group()
            objects = pygame.sprite.Group()

            parse_level(level)

            all_sprites.add(floor)
            all_sprites.add(player)
        if player.rect.colliderect(object.rect) and object.standable:
            player.speedy = object.rect.y - player.rect.y - player.rect.size[1] + 1
            player.update()
            player.speedy = 0
            if keys[pygame.K_SPACE]:
                player.speedy = -15

    player.speedy += 1

    all_sprites.update()
    all_sprites.draw(window)

    # _______

    pygame.display.flip()
    clock.tick(60)

pygame.quit()