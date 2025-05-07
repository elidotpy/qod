import pygame

# initiating
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.init()

# setting window up
proportions = 800, 600
window = pygame.display.set_mode(proportions)

class PlayButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([100,100])
        self.image.fill("green")
        self.rect = self.image.get_rect()
        self.rect.x = proportions[0] // 2 - self.rect.size[0] // 2
        self.rect.y = proportions[1] // 2 - self.rect.size[1] // 2

    def pressed(self):
        return "levellist"

def LevelList():
    global running
    buttons = pygame.sprite.Group()

    buttons.add(PlayButton())

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.rect.collidepoint(mouse_pos):
                        return button.pressed()

        window.fill("black")

        # render here
        buttons.draw(window)
        # _______

        pygame.display.flip()
        clock.tick(60)

def MainMenu():
    global running
    buttons = pygame.sprite.Group()

    buttons.add(PlayButton())

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.rect.collidepoint(mouse_pos):
                        return button.pressed()

        window.fill("black")

        # render here
        buttons.draw(window)
        # _______

        pygame.display.flip()
        clock.tick(60)

running = True

state = "menu"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if state == "menu":
        state = MainMenu()
    elif state == "levellist"?

pygame.quit()