import pygame
import os
from ship import Ship
from planet import Planet
from star import Star
import random as r

# Define constants
WIDTH, HEIGHT = 1800, 1000
HW, HH = WIDTH/2, HEIGHT/2
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255,255,255)
BLUE = (0,0,30)
FPS = 60
SPRITE_DELAY = 5 # Sprite delay is the delay in how frequently the background stars animate
NUM_STARS = 7

SHIP = pygame.image.load(os.path.join('img', 'ship.png')).convert_alpha()
PLANET = pygame.image.load(os.path.join('img', 'planet2.png')).convert_alpha()


pygame.display.set_caption("moonland")

# Draws all objects onto window
def drawWindow(ship, ship_center, planets, bg_sprites,count):
    WIN.fill(BLUE)

    # Background stars animations are bg_sprites, the animation frame rate is set to every SPRITE_DELAY ticks
    bg_sprites.draw(WIN)
    if count % SPRITE_DELAY == 0:
        bg_sprites.update()
    WIN.blit(ship, ship_center)

    planets.draw(WIN)
    pygame.display.update()

def main():

    clock = pygame.time.Clock()

    run = True

    ship = Ship(SHIP, 2, 0.1, 300, 300, 0)
    p1 = Planet(400, PLANET, 0.5, HW, HH)
    p2 = Planet(200, PLANET, 0.2, 600, 200)
    ship.addPlanet(p1)
    ship.addPlanet(p2)

    planets = pygame.sprite.Group()
    planets.add(p1)
    planets.add(p2)

    bg_sprites = pygame.sprite.Group()

    # Randomly generate stars with different animation frequencies and locations
    for i in range(NUM_STARS):
        star = Star(r.randint(0, WIDTH),r.randint(0, HEIGHT), r.randint(15,50))
        bg_sprites.add(star)

    # Count keeps track of the ticks, for slowing down sprite animation so the FPS is easier to see
    count = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Detect if ship has collided with any planets
        hit = pygame.sprite.spritecollide(ship, planets, False, pygame.sprite.collide_circle)
        
        # If no collision, continue movement and control input
        if hit:
            ship.stop()
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
        
        drawWindow(ship.getShip(), ship.getCoords(), planets, bg_sprites, count)            

        count = (count % SPRITE_DELAY) + 1


    pygame.quit()

if __name__ == "__main__":
    main()