import pygame
from sys import exit


# Function To display the current score
def show_score():
    current_score = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = defaultfont.render(f'SCORE: {current_score}', False, 'Black')
    score_rect = score_surface.get_rect(center = (700, 50))
    screen.blit(score_surface, score_rect)
    return current_score

# Animating the Zombie walk and jump
def zombie_animation():
    global zombie, zombie_index

    if zombie_rect.bottom < 310:
        zombie = zombie_jump
    else:
        zombie_index += 0.1
        if zombie_index >= len(zombie_walk): zombie_index = 0
        zombie = zombie_walk[int(zombie_index)]

# Initialize pygame utilities
pygame.init()

# Creating the display screen where the gameplay happens 
# Along with the window resolution 800x400
screen = pygame.display.set_mode((800, 400))

# Update Pygame Window title
pygame.display.set_caption("Zombie Runner")

# Update Custom pygame icon
pygame_icon = pygame.image.load('graphics/thorn.png')
pygame.display.set_icon(pygame_icon)

# creating clock object to set the framerate in while loop
clock = pygame.time.Clock()

test_font = pygame.font.Font('fonts/BloodyTerror.ttf', 25)
defaultfont = pygame.font.Font('fonts/MontserratRegular-BWBEl.ttf', 24)

is_game_active = True
start_time = 0

# creating background surface of the game
width = 800
height = 400
sky_surface = pygame.image.load('Images/surface.png').convert_alpha()
sky_surface = pygame.transform.scale(sky_surface, (width, height))


# Create characters, specify the position and movements

thorn = pygame.image.load('graphics/thorn.png').convert_alpha()
thorn_rect = thorn.get_rect(bottomright = (650, 310))

zombie_walk1 = pygame.image.load('Images/zombie/Idle (15).png')
zombie_walk2 = pygame.image.load('Images/zombie/Walk (1).png')
zombie_walk3 = pygame.image.load('Images/zombie/Walk (2).png')
zombie_walk4 = pygame.image.load('Images/zombie/Walk (3).png')
zombie_walk5 = pygame.image.load('Images/zombie/Walk (4).png')
zombie_walk6 = pygame.image.load('Images/zombie/Walk (5).png')
zombie_walk7 = pygame.image.load('Images/zombie/Walk (6).png')
zombie_walk8 = pygame.image.load('Images/zombie/Walk (7).png')
zombie_walk9 = pygame.image.load('Images/zombie/Walk (8).png')
zombie_walk10 = pygame.image.load('Images/zombie/Walk (9).png')

zombie_walk = [zombie_walk1, zombie_walk2, zombie_walk3, zombie_walk9, zombie_walk10]
zombie_index = 0
zombie_jump = pygame.image.load('Images/zombie/Walk (9).png')

zombie = zombie_walk[zombie_index]
zombie_rect = zombie.get_rect(midbottom = (100, 310))
zombie_gravity = 0

# Game over screen design
game_over_text = test_font.render('GAME OVER', False, 'Red')
restart_text = defaultfont.render('Hit SPACE to Restart', False, 'Black')
game_over_text_rect = game_over_text.get_rect(center = (400, 150))
restart_text_rect = restart_text.get_rect(center = (400, 250))


# main loop
i = 0
while True:
    # Events for the gameplay
    # To Close the pygame if quit event has been called
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # To close the while loop properly with exit() method in sys module

        if is_game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and zombie_rect.bottom == 310:
                zombie_gravity = -15

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and zombie_rect.bottom == 310:
                    zombie_gravity = -15

        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_game_active = True
                thorn_rect.left = 800

    if is_game_active:
        # Draw all elements to the window

        # Creating the regular surface
        screen.blit(sky_surface, (i, 0))
        screen.blit(sky_surface,(width+i,0))
        if (i==-width):
            screen.blit(sky_surface,(width+i,0))
            i=0
        i-=1

        show_score()
        
        thorn_rect.x -= 4
        if thorn_rect.right <=0:
            thorn_rect.left = 800
        screen.blit(thorn, thorn_rect)

        zombie_gravity += 1
        zombie_rect.y += zombie_gravity
        if zombie_rect.bottom >= 310: 
            zombie_rect.bottom = 310
        
        zombie_animation()
        
        screen.blit(zombie, zombie_rect)

        # Collision 
        if zombie_rect.colliderect(thorn_rect):
            is_game_active = False
            final = int(pygame.time.get_ticks() / 1000) - start_time
            final_score = test_font.render(f'You Scored - {final} points', False, 'Red')
            final_score_rect = final_score.get_rect(center = (400, 200))
            start_time = 0
    
    else:
        screen.fill('#EFE7BC')
        screen.blit(game_over_text, game_over_text_rect)
        screen.blit(restart_text, restart_text_rect)
        screen.blit(final_score, final_score_rect)
        start_time = int(pygame.time.get_ticks() / 1000)
        


    # To update all the draw we perform in play window
    pygame.display.update()
    clock.tick(60)