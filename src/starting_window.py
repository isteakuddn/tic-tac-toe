import sys
import pygame

pygame.init()

# --- 1. Colors and Constants ---
OFF_WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# --- 2. Setup ---
base_font = pygame.font.Font(None, 32)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Resizable')

# --- 3. Load Assets and Define Rects ---
cross_image = pygame.image.load("images/cross_image.png")
circle_image = pygame.image.load("images/circle_image.png")

# Variables for the "Cross" player input
cross_player_name = ""
cross_player_name_input = pygame.Rect(150, 80, 175, 55)
cross_active = False

# Variables for the "Circle" player input
circle_player_name = ""
circle_player_name_input = pygame.Rect(150, 180, 175, 55)
circle_active = False

# --- 4. Main Game Loop ---
program_running = True

while program_running:
    # --- 5. Event Handling (With 10 Char Limit) ---
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
            # --- Handle typing for the CROSS player ---
            if cross_active:
                if event.key == pygame.K_BACKSPACE:
                    cross_player_name = cross_player_name[:-1]
                else:
                    # Only add char if length is less than 10
                    if len(cross_player_name) < 10:
                        cross_player_name += event.unicode
            
            # --- Handle typing for the CIRCLE player ---
            if circle_active:
                if event.key == pygame.K_BACKSPACE:
                    circle_player_name = circle_player_name[:-1]
                else:
                    # Only add char if length is less than 10
                    if len(circle_player_name) < 10:
                        circle_player_name += event.unicode
    
    # --- 6. Drawing ---
    screen.fill(OFF_WHITE)

    # --- Draw Cross Player Box ---
    screen.blit(cross_image,(80, 80))
    if cross_active:
        cross_color = color_active
    else:
        cross_color = color_passive
    pygame.draw.rect(screen, cross_color, cross_player_name_input, 2)

    # --- Draw Circle Player Box ---
    screen.blit(circle_image, (80, 180))
    if circle_active:
        circle_color = color_active
    else:
        circle_color = color_passive
    pygame.draw.rect(screen, circle_color, circle_player_name_input, 2)

    # --- 7. Render and Draw Text (With Vertical Centering) ---
    
    # Render the CROSS text
    cross_text_surface = base_font.render(cross_player_name, True, BLACK)
    cross_text_y = cross_player_name_input.y + (cross_player_name_input.h - cross_text_surface.get_height()) // 2
    # NEW: Increased padding from 5 to 10
    screen.blit(cross_text_surface, (cross_player_name_input.x + 10, cross_text_y))

    # Render the CIRCLE text
    circle_text_surface = base_font.render(circle_player_name, True, BLACK)
    circle_text_y = circle_player_name_input.y + (circle_player_name_input.h - circle_text_surface.get_height()) // 2
    # NEW: Increased padding from 5 to 10
    screen.blit(circle_text_surface, (circle_player_name_input.x + 10, circle_text_y))


    # --- 8. Update Screen ---
    pygame.display.flip()

# --- 9. Quit ---
pygame.quit()
sys.exit()