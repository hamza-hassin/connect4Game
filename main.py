import pygame
import time
from setting import *
from player import *

pygame.init()

screen = pygame.display.set_mode((900, 700))

pygame.display.set_caption(" Puissance 4  game ")

pygame.display.set_icon(icon)

pos = pygame.mouse.get_pos()
run = True
first = False
second = False
x = 174
y = 212


def start_menu():
    start = True
    while start:
        screen.fill((255, 255, 255))


while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if Column1.collidepoint(event.pos):
                first = True
        if event.type == pygame.MOUSEBUTTONUP:
            if Column2.collidepoint(event.pos):
                second = True
    screen.fill((100, 200, 5))

    if first:
        screen.blit(redBall, (x, y))

    if second:
        screen.blit(blackBall, (20 + x + 69, -6 + y))
    screen.blit(board_img, (160, 200))
    pygame.display.update()

pygame.quit()
