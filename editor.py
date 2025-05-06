import pygame

# initiating
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.init()

# setting window up
proportions = 800, 600
window = pygame.display.set_mode(proportions)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill("black")

    # render here

    # _______

    pygame.display.flip()
    clock.tick(60)

pygame.quit()