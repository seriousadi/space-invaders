import pygame
import os

pygame.init()
screen = pygame.display.set_mode((350, 550))
clock = pygame.time.Clock()
shoot = False
y = 400
running = True
to_remove = []

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
    locations = []
    for n in range(0, 300, 40):
        for m in range(0, 200, 40):
            locations.append((n, m))
    aliens = []
    for n in locations:
        if locations.index(n) not in to_remove:
            alien1 = pygame.image.load(os.path.join('Images', 'alien-1295484_1280.png')).convert_alpha()
            alien = screen.blit(alien1, n)
            aliens.append(alien)
    # creating Shooter
    mouse_x_loc = pygame.mouse.get_pos()[0]
    shooter = pygame.image.load(os.path.join('Images', 'tank-3567419_1920.png')).convert_alpha()
    screen.blit(shooter, (mouse_x_loc, 400))

    # mouse Clicked checking
    mouse_left_click = pygame.mouse.get_pressed()[0]

    if mouse_left_click and y == 400:
        shoot = True
        shooted_from = mouse_x_loc

    if shoot:
        bullet_up = pygame.image.load(os.path.join('Images', 'bullet-up.png')).convert_alpha()
        bullet_up = screen.blit(bullet_up, (shooted_from + 23, y))
        y -= 10
        collided_with = bullet_up.collidelistall(aliens)
        if y < 1 or len(collided_with) > 0:
            y = 400
            shoot = False
            if len(collided_with) > 0:
                for n in collided_with:
                    print(n)
                    to_remove.append(n)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(20)  # limits FPS to 60

pygame.quit()
