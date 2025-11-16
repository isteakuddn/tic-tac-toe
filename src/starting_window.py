import sys
import pygame

pygame.init()

RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Resizable')
# Icon = pygame.image.load('src/example.jpg')
# pygame.display.set_icon(Icon)

cross_image = pygame.image.load("images/cross_image.png")
cross_player_name = ""
cross_player_name_input = pygame.Rect(150, 85, 155, 45)

circle_image = pygame.image.load("images/circle_image.png")
circle_player_name = ""
circle_player_name_input = pygame.Rect(150, 185, 155, 45)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(RED)

    screen.blit(cross_image,(80, 80))
    pygame.draw.rect(screen, BLUE, cross_player_name_input)
    
    screen.blit(circle_image, (80, 180))
    pygame.draw.rect(screen, BLUE, circle_player_name_input)

    pygame.display.flip()

pygame.quit()