import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fake Free Fire Offline")

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Player settings
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - 100
player_speed = 5

# Bullet settings
bullets = []
bullet_speed = 7

# Enemy settings
enemies = []
enemy_size = 50
enemy_speed = 3

score = 0
font = pygame.font.SysFont(None, 36)

def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, player_size, player_size))

def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, (x, y, enemy_size, enemy_size))

def draw_bullet(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, 5, 10))

def show_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over():
    text = font.render("GAME OVER", True, RED)
    screen.blit(text, (WIDTH//2 - 80, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Main game loop
while True:
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + player_size//2, player_y])

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_speed

    # Spawn enemies
    if random.randint(1, 40) == 1:
        enemies.append([random.randint(0, WIDTH - enemy_size), 0])

    # Move bullets
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Move enemies
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)

    # Collision detection
    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if (enemy[0] < bullet[0] < enemy[0] + enemy_size and
                enemy[1] < bullet[1] < enemy[1] + enemy_size):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 1
                break

        # Player collision
        if (enemy[0] < player_x + player_size and
            enemy[0] + enemy_size > player_x and
            enemy[1] < player_y + player_size and
            enemy[1] + enemy_size > player_y):
            game_over()

    # Draw everything
    draw_player(player_x, player_y)

    for bullet in bullets:
        draw_bullet(bullet[0], bullet[1])

    for enemy in enemies:
        draw_enemy(enemy[0], enemy[1])

    show_score()

    pygame.display.update()
    clock.tick(60)