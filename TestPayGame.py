import pygame
import time

pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Test Pay Game")

image1 = pygame.image.load("PyShark.png")
image_rect1 = image1.get_rect()

image2 = pygame.image.load("010102.png")
image_rect2 = image2.get_rect()

# speed = 5

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect1.x = mouseX - 100
            image_rect1.y = mouseY - 150

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     image_rect.x -= speed
    # if keys[pygame.K_RIGHT]:
    #     image_rect.x += speed
    # if keys[pygame.K_UP]:
    #     image_rect.y -= speed
    # if keys[pygame.K_DOWN]:
    #     image_rect.y += speed

    screen.fill((0, 0, 0))
    screen.blit(image1, image_rect1)
    screen.blit(image2, image_rect2)

    if image_rect1.colliderect(image_rect2):
        print("<BBBoooooooMMM!!!>")
        time.sleep(1)

    pygame.display.flip()

pygame.quit()
