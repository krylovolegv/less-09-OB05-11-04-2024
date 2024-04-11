import pygame
import random

# Initialize PyGame
pygame.init()

# Game Parameters
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 854
BLOCK_SIZE = 20
SPEED = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ZMEYKA")
clock = pygame.time.Clock()

snake_image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
snake_image.fill(GREEN)
food_image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
food_image.fill(RED)
bg_image = pygame.image.load('background.jpg').convert()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


class Block:
    def __init__(self, rect):
        self.rect = rect


def generate_random_point():
    return pygame.Rect(random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE),
                       random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE),
                       BLOCK_SIZE, BLOCK_SIZE)


def update_snake(snake_body, dx, dy):
    global food
    head = snake_body[0]
    new_rect = head.rect.move(dx, dy)
    new_head = Block(new_rect)
    return new_head


def check_collision(rect, snake_body):
    if rect.left < 0 or rect.right > SCREEN_WIDTH or rect.top < 0 or rect.bottom > SCREEN_HEIGHT:
        return True
    for block in snake_body[1:]:
        if block.rect.colliderect(rect):
            return True
    return False


snake_body = [Block(pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BLOCK_SIZE, BLOCK_SIZE))]
food = generate_random_point()

dx, dy = 0, 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dx, dy = 0, -BLOCK_SIZE
            elif event.key == pygame.K_DOWN:
                dx, dy = 0, BLOCK_SIZE
            elif event.key == pygame.K_LEFT:
                dx, dy = -BLOCK_SIZE, 0
            elif event.key == pygame.K_RIGHT:
                dx, dy = BLOCK_SIZE, 0

    new_head = update_snake(snake_body, dx, dy)
    if check_collision(new_head.rect, snake_body):
        print("Game Over")
        break

    snake_body.insert(0, new_head)
    if new_head.rect.colliderect(food):
        food = generate_random_point()
    else:
        snake_body.pop()

    screen.blit(bg_image, (0, 0))

    for block in snake_body:
        screen.blit(snake_image, (block.rect.x, block.rect.y))

    screen.blit(food_image, (food.x, food.y))

    pygame.display.flip()
    clock.tick(SPEED)

pygame.quit()

