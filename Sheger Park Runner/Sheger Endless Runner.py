
import pygame
from sys import exit
from random import randint

# Show score on screen
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f' ነጥብ: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    return current_time

# Change player image
def player_animation():
    global player_surf, player_index
    if player_rect.bottom < 320:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('የሸገር ፓርክ ሯጭ')
clock = pygame.time.Clock()
test_font = pygame.font.Font('NotoSansEthiopic[wdth,wght].ttf', 25)
game_active = False
start_time = 0
score = 0
high_score = 0

# Background
sky_surface = pygame.image.load('skyyy.jpg')
ground_surface1 = pygame.image.load('rooaadd.jpg').convert()
ground_surface2 = pygame.image.load('rooad.jpg').convert()

# Obstacles
obstacle1_surface = pygame.image.load('obstaclle.jpg').convert_alpha()
fly_surf1 = pygame.image.load('fly1-removebg-preview.png').convert_alpha()
fly_surf2 = pygame.image.load('fly2-removebg-preview.png').convert_alpha()
fly_index = 0

# Player
player_walk1 = pygame.image.load('step1-removebg-preview (1).png').convert_alpha()
player_walk2 = pygame.image.load('step2-removebg-preview.png').convert_alpha()
player_walk3 = pygame.image.load('step3-removebg-preview.png').convert_alpha()
player_walk = [player_walk1, player_walk2, player_walk3]
player_index = 0
player_surf = player_walk[player_index]
player_jump = pygame.transform.scale(player_walk1, player_walk1.get_size())
player_rect = player_surf.get_rect(topleft=(80, 220))
player_gravity = 0

# Start screen
player_stand = pygame.image.load('step2-removebg-preview.png').convert_alpha()
player_stand_scaled = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center=(400, 130))

# Decorations
tree_surf = pygame.image.load('stree-removebg-preview.png').convert_alpha()
chair_surf = pygame.image.load('chair-removebg-preview (1).png').convert_alpha()
chair_surf = pygame.transform.scale(chair_surf, (60, 50))
pole_surf = pygame.image.load('lamp-removebg-preview.png').convert_alpha()
pole_surf  = pygame.transform.scale(pole_surf, (60, 90))
pole_surf1 = pygame.image.load('lamp-removebg-preview.png').convert_alpha()
pole_surf1 = pygame.transform.scale(pole_surf, (60, 90))
new_tree_surf = pygame.image.load('tree-removebg-preview.png').convert_alpha()
new_tree_surf = pygame.transform.scale(new_tree_surf, (60, 50))
tree_surf1 = pygame.image.load('stree-removebg-preview.png').convert_alpha()
flower_surf = pygame.image.load('flower-removebg-preview.png').convert_alpha()
flower_surf = pygame.transform.scale(flower_surf, (120, 30)) 
flower_surf1 = pygame.image.load('flower-removebg-preview.png').convert_alpha()
flower_surf1 = pygame.transform.scale(flower_surf, (120, 30)) 
new_tree_surf1 = pygame.image.load('tree-removebg-preview.png').convert_alpha()
new_tree_surf1 = pygame.transform.scale(new_tree_surf, (60, 50))
tree_surf2 = pygame.image.load('stree-removebg-preview.png').convert_alpha()
chair_surf2 = pygame.image.load('chair-removebg-preview (1).png').convert_alpha()
chair_surf2 = pygame.transform.scale(chair_surf2, (60, 50))
new_tree_surf2 = pygame.image.load('tree-removebg-preview.png').convert_alpha()
new_tree_surf2 = pygame.transform.scale(new_tree_surf, (60, 50))

# Amharic texts
game_name = test_font.render('የሸገር ፓርክ ሯጭ', False, (0, 0, 0))
game_name_rect = game_name.get_rect(center=(400, 50))
game_messege = test_font.render('ለመሮጥ ስፔስ ባር ይጫኑ', False, (0, 0, 0))
game_messege_rect = game_messege.get_rect(center=(400, 280))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)
obstacle_rect_list = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                obstacle_rect_list.clear()
                start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == obstacle_timer and game_active:
            if randint(0, 1):
                obstacle_rect_list.append(obstacle1_surface.get_rect(bottomright=(800, 320)))
            else:
                obstacle_rect_list.append(fly_surf1.get_rect(bottomright=(800, 200)))

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface1, (0, 290))
        screen.blit(ground_surface2, (700, 290))
        score = display_score()

        # Decorations
        screen.blit(tree_surf, (280, 270))
        screen.blit(pole_surf, (345, 205))
        screen.blit(chair_surf, (80, 250))
        screen.blit(new_tree_surf, (445, 250))
        screen.blit(tree_surf1, (0, 270))
        screen.blit(flower_surf, (140, 270))
        screen.blit(new_tree_surf1, (750, 250))
        screen.blit(tree_surf2, (670, 270))
        screen.blit(chair_surf2, (400, 250))
        screen.blit(new_tree_surf2, (250, 250))
        screen.blit(flower_surf1, (505, 270))
        screen.blit(pole_surf1, (580, 205))

        # Fly animation
        fly_index += 0.1
        if fly_index >= 2: fly_index = 0

        # Obstacles
        for obstacle_rect in obstacle_rect_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 320:
                screen.blit(obstacle1_surface, obstacle_rect)
            else:
                if int(fly_index) == 0:
                    screen.blit(fly_surf1, obstacle_rect)
                else:
                    screen.blit(fly_surf2, obstacle_rect)

        # Remove off-screen
        obstacle_rect_list = [ob for ob in obstacle_rect_list if ob.x > -100]

        # Collision
        for obstacle_rect in obstacle_rect_list:
            if player_rect.colliderect(obstacle_rect):
                game_active = False

        # Gravity
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 320:
            player_rect.bottom = 320

        # Player
        player_animation()
        screen.blit(player_surf, player_rect)

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand_scaled, player_stand_rect)
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_messege, game_messege_rect)
        else:
            if score > high_score:
                high_score = score
            score_message = test_font.render(f'ነጥብ: {score}', False, (0, 0, 0))
            score_message_rect = score_message.get_rect(center=(400, 8))
            high_score_message = test_font.render(f'ከፍተኛ ነጥብ: {high_score}', False, (0, 0, 0))
            high_score_rect = high_score_message.get_rect(center=(400, 300))
            screen.blit(score_message, score_message_rect)
            screen.blit(high_score_message, high_score_rect)
            screen.blit(game_messege, game_messege_rect)

    pygame.display.update()
    clock.tick(60)