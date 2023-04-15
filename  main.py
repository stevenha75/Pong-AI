import pygame
from pong import Game

# Creating window
width, height = 700, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("AI Pong by Steven Ha")

game = Game(window, width, height)

run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    game.loop()
    game.draw()
    pygame.display.update()
    
pygame.quit()