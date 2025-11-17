import sys
import pygame

pygame.init()

OFF_WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

base_font = pygame.font.Font(None, 32)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Resizable')

cross_image = pygame.image.load("images/cross_image.png")
circle_image = pygame.image.load("images/circle_image.png")

cross_player_name = ""
cross_player_name_input = pygame.Rect(150, 80, 175, 55)
cross_active = False

circle_player_name = ""
circle_player_name_input = pygame.Rect(150, 180, 175, 55)
circle_active = False

program_running = True

while program_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if cross_player_name_input.collidepoint(event.pos):
                cross_active = True
                circle_active = False
            elif circle_player_name_input.collidepoint(event.pos):
                cross_active = False
                circle_active = True
            else:
                cross_active = False
                circle_active = False
        
        if event.type == pygame.KEYDOWN:
            if cross_active:
                if event.key == pygame.K_BACKSPACE:
                    cross_player_name = cross_player_name[:-1]
                else:
                    if len(cross_player_name) < 10:
                        cross_player_name += event.unicode
            
            if circle_active:
                if event.key == pygame.K_BACKSPACE:
                    circle_player_name = circle_player_name[:-1]
                else:
                    if len(circle_player_name) < 10:
                        circle_player_name += event.unicode
    
    screen.fill(OFF_WHITE)

    screen.blit(cross_image,(80, 80))
    if cross_active:
        cross_color = color_active
    else:
        cross_color = color_passive
    pygame.draw.rect(screen, cross_color, cross_player_name_input, 2)

    screen.blit(circle_image, (80, 180))
    if circle_active:
        circle_color = color_active
    else:
        circle_color = color_passive
    pygame.draw.rect(screen, circle_color, circle_player_name_input, 2)

    
    cross_text_surface = base_font.render(cross_player_name, True, BLACK)
    cross_text_y = cross_player_name_input.y + (cross_player_name_input.h - cross_text_surface.get_height()) // 2

    screen.blit(cross_text_surface, (cross_player_name_input.x + 10, cross_text_y))


    circle_text_surface = base_font.render(circle_player_name, True, BLACK)
    circle_text_y = circle_player_name_input.y + (circle_player_name_input.h - circle_text_surface.get_height()) // 2

    screen.blit(circle_text_surface, (circle_player_name_input.x + 10, circle_text_y))


    pygame.display.flip()

pygame.quit()
sys.exit()