from img import scaleImg
import pygame
import os
from ship import Ship
from planet import Planet
from star import Star
import random as r
from button import Button

# Define constants
WIDTH, HEIGHT = 1800, 1000
HW, HH = WIDTH/2, HEIGHT/2
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255,255,255)
BLUE = (0,0,20)
FPS = 60
SPRITE_DELAY = 5 # Sprite delay is the delay in how frequently the background stars animate
NUM_STARS = 7

# RIP message after player crashes
RIP = scaleImg(pygame.image.load(os.path.join('img', 'rip.png')), 5)
RIP_RECT = RIP.get_rect()

# Retry button after player crashes
RETRY_IMG = scaleImg(pygame.image.load(os.path.join('img', 'retry.png')).convert_alpha(), 2)
RETRY_HOVER_IMG = scaleImg(pygame.image.load(os.path.join('img', 'retry_hover.png')).convert_alpha(), 2)
RETRY_CLICKED_IMG = scaleImg(pygame.image.load(os.path.join('img', 'retry_clicked.png')).convert_alpha(), 2)
RETRY = Button(HW, HH, RETRY_IMG, RETRY_HOVER_IMG, RETRY_CLICKED_IMG)

# Load ship and planet
SHIP = pygame.image.load(os.path.join('img', 'ship.png'))
PLANET = pygame.image.load(os.path.join('img', 'planet2.png'))


pygame.display.set_caption("moonland")

# Draws all objects onto window
def drawWindow(ship, ship_center, planets, bg_sprites,count, game_over, rip_y):
    WIN.fill(BLUE)

    # Background stars animations are bg_sprites, the animation frame rate is set to every SPRITE_DELAY ticks
    bg_sprites.draw(WIN)
    if count % SPRITE_DELAY == 0:
        bg_sprites.update()
    WIN.blit(ship, ship_center)

    planets.draw(WIN)

    # Add game over message and retry button
    if game_over:
        WIN.blit(RIP,(HW - (RIP_RECT.width/2), rip_y))

        if rip_y >= HH - (RIP_RECT.height/2) - 200:
            if RETRY.handle_click(WIN):
                main()

    pygame.display.update()

def main():

    clock = pygame.time.Clock()

    run = True

    ship = Ship(SHIP, 0.7, 0.1, 300, 300, 0)
    p1 = Planet(100, PLANET, 0.3, HW, HH)
    p2 = Planet(100, PLANET, 0.2, 600, 200)
    ship.addPlanet(p1)
    ship.addPlanet(p2)

    # y position of RIP png after game over
    rip_y = -500

    planets = pygame.sprite.Group()
    planets.add(p1)
    planets.add(p2)

    # background sprites contains all the background animations happening during the game
    bg_sprites = pygame.sprite.Group()

    # Randomly generate stars with different animation frequencies and locations
    for i in range(NUM_STARS):
        star = Star(r.randint(0, WIDTH),r.randint(0, HEIGHT), r.randint(15,50))
        bg_sprites.add(star)

    # Every time count reaches SPRITE_DELAY, a sprite animation frame occurs and count is set back to 0
    # This helps slow down the FPS of the sprite animations so the sprite FPS != game FPS
    count = 0
    
    # If exploded becomes true, begin explosion animation
    exploded = False

    # If game_over is true, display game over and retry button
    game_over = False

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        

        if not exploded:
            # Detect if ship has collided with any planets
            hit = pygame.sprite.spritecollide(ship, planets, False, pygame.sprite.collide_circle)

            # If no collision, continue movement and control input
            if hit:
                ship.stop()
                exploded = True
            else:
                inputs = pygame.key.get_pressed()

                if inputs[pygame.K_LEFT]:
                    ship.rotateImg(5)
                
                if inputs[pygame.K_RIGHT]:
                    ship.rotateImg(-5)

                if inputs[pygame.K_SPACE]:
                    # Need the isAccelerating function for the acceleration animation
                    ship.isAccelerating(True)
                    ship.accelerate()
                else:
                    ship.isAccelerating(False)


                # Passive move includes the ships acceleration due to input, as well as gravity from nearby planets
                ship.passiveMove()
        else:
            # Begin explosion animation. game_over is false during the animation, and true after the animation
            game_over = ship.explode()

            # Update position of RIP rect to scroll downward
            if rip_y < HH - (RIP_RECT.height/2) - 200:
                rip_y += 8

        drawWindow(ship.getShip(), ship.getCoords(), planets, bg_sprites, count, game_over, rip_y)            

        count = (count % SPRITE_DELAY) + 1


    pygame.quit()

if __name__ == "__main__":
    main()