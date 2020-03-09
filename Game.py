import pygame
import random
import os
import Snake as snk
import Food as fd
import Piece as pic


def drawGrid():
    pass
    # for column in range(0, 600, 20):
    #     for row in range(0, 600, 20):
    #         pygame.draw.rect(screen, (0, 0, 255), [column, row, 19, 19])


os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

size = width, height = 600, 600
speed = 20
clock = pygame.time.Clock()
fps = 25
direction = [speed, 0]
axes = [True, False]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

snake = snk.Snake([width/2 + 10, height/2 + 10])
snake_group = pygame.sprite.Group()
food_group = pygame.sprite.Group()
tail_group = pygame.sprite.Group()
snake_group.add(snake)

pos = [x for x in range(10, 590, 20)]
food = fd.Food([random.choice(pos), random.choice(pos)])
food_group.add(food)
snake.vx = width/2
snake.vy = height/2

snake_tail = []


is_playing = True

pygame.time.wait(1000)

while is_playing:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and axes[0]:
                direction = [0, speed]
                axes = [False, True]
            if event.key == pygame.K_UP and axes[0]:
                direction = [0, -speed]
                axes = [False, True]
            if event.key == pygame.K_RIGHT and axes[1]:
                direction = [speed, 0]
                axes = [True, False]
            if event.key == pygame.K_LEFT and axes[1]:
                direction = [-speed, 0]
                axes = [True, False]
            if event.key == pygame.K_r:
                pygame.quit()
                os.system('python Game.py')
            if event.key == pygame.K_q:
                is_playing = False

    snake.rect.x += direction[0]
    snake.rect.y += direction[1]

    if snake.rect.x < 0 or snake.rect.x > width - 20:
        is_playing = False
    if snake.rect.y < 0 or snake.rect.y > height - 20:
        is_playing = False

    hit = pygame.sprite.spritecollide(snake, food_group, True)

    if hit:
        food.kill()
        snake.pieces += 1
        check_spawn = True
        spawn = []
        while check_spawn:
            spawn = [random.choice(pos), random.choice(pos)]
            check_spawn = False
            for i in snake_tail:
                p_pos = i.getPosition()
                if spawn[0] == p_pos[0] and spawn[1] == p_pos[1]:
                    check_spawn = True
        food = fd.Food(spawn)
        food_group.add(food)

    hit = pygame.sprite.spritecollide(snake, tail_group, True)

    if hit:
        is_playing = False

    snake_tail.append(pic.Piece([snake.rect.x + 10, snake.rect.y + 10], snake.pieces))

    screen.fill(black)
    drawGrid()
    for i in snake_tail:
        tail_group.add(i)
        x = i.decreaseCycle()
        if x == 0:
            snake_tail.remove(i)
            i.kill()
    tail_group.draw(screen)
    snake_group.draw(screen)
    food_group.draw(screen)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
