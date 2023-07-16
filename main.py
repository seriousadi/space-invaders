import pygame
import os

pygame.init()
screen = pygame.display.set_mode((350, 550))
screen_x, screen_y = screen.get_size()

clock = pygame.time.Clock()
shoot = False
bullet_y = 400  # bullet starting location at y-axis
running = True
aliens_to_remove = []
alien_x = 0
alien_y = 0
move_left = 1
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    # Creating aliens
    aliens_cooridinates = []
    aliens = []
    total_aliens  = 0
    for n in range(0, 300, 40):
        for m in range(0, 200, 40):
            aliens_cooridinates.append((n + alien_x, m + alien_y))
            total_aliens +=1

    for n in aliens_to_remove:
        aliens_cooridinates.pop(n)

    for n in aliens_cooridinates:
        alien1 = pygame.image.load(os.path.join('Images', 'alien-1295484_1280.png')).convert_alpha()
        alien = screen.blit(alien1, n)
        aliens.append(alien)

    # creating Shooter
    mouse_x_loc = pygame.mouse.get_pos()[0]
    shooter = pygame.image.load(os.path.join('Images', 'tank-3567419_1920.png')).convert_alpha()
    screen.blit(shooter, (mouse_x_loc, 400))

    # mouse Clicked checking
    mouse_left_click = pygame.mouse.get_pressed()[0]

    if mouse_left_click and bullet_y == 400:
        shoot = True
        shooted_from = mouse_x_loc

    if shoot:
        bullet_up = pygame.image.load(os.path.join('Images', 'bullet-up.png')).convert_alpha()
        bullet_up = screen.blit(bullet_up, (shooted_from + 23, bullet_y))
        bullet_y -= 10
        collided_with = bullet_up.collidelistall(aliens)
        if bullet_y < 1 or len(collided_with) > 0:
            bullet_y = 400
            shoot = False
            if len(collided_with) > 0:
                for n in collided_with:
                    aliens_to_remove.append(n)

    alien_x += move_left
    for n in aliens:
        if n.x > screen_x - 30:
            move_left = -1

            alien_y += 3
            break
        if n.x < 3:
            move_left = 1
            alien_y += 3
            break
        if n.y > 370:
            running = False
            print("You've lost")

    if len(aliens_to_remove) ==total_aliens:
        running =False
        print("You've won")
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(20)  # limits FPS to 60

pygame.quit()
