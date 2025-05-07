import os
import pygame
from classes import Block, Object
from utils import paginate

# initiating
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.init()

# setting window up
proportions = 800, 600
window = pygame.display.set_mode(proportions)

running = True

objects = pygame.sprite.Group()
spacing = 0
object_size = 50

blocks_found = os.listdir("assets/blocks")
pages = paginate(5, blocks_found)

def get_objects_at_page(index: int):
    spacing = 0
    x = proportions[0] // len(pages[index]) - object_size - object_size / 2
    start_x = x

    for block in pages[index]:
        if block.endswith(".png"):
            x += object_size
            objects.add(
                Block(x + spacing, 540, int(block.split(".")[0]), f"assets/blocks/{block}")
            )
            spacing += proportions[0] // len(pages[index]) - object_size * 2

    return Object(
        start_x + (object_size + 10),
        595,
        width=object_size - 20,
        height=5
    )

page_index = 0
chosen = get_objects_at_page(page_index)
divisor = Object(0, 530, width=800, height=600, color=(32,32,32))

left_button = Object(0, 540, "assets/buttons/left.png")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for block in objects:
                if block.rect.collidepoint(mouse_pos):
                    chosen.rect.x = block.rect.x + 10

    window.fill("black")

    # render here
    divisor.draw(window)
    objects.draw(window)
    chosen.draw(window)
    left_button.draw(window)
    # _______

    pygame.display.flip()
    clock.tick(60)

pygame.quit()