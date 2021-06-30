import pygame
import os
from ship import Ship
from planet import Planet
from star import Star
import random as r


WIDTH, HEIGHT = 1800, 1000
HW, HH = WIDTH/2, HEIGHT/2
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255,255,255)
BLUE = (0,0,30)
FPS = 60
SPRITE_DELAY = 5
NUM_STARS = 7

SHIP = pygame.image.load(os.path.join('img', 'ship.png')).convert_alpha()
PLANET = pygame.image.load(os.path.join('img', 'planet2.png')).convert_alpha()


pygame.display.set_caption("moonland")

def drawWindow(ship, ship_center, planet, planet_center, bg_sprites,count):
    WIN.fill(BLUE)
    bg_sprites.draw(WIN)
    if count % SPRITE_DELAY == 0:
        bg_sprites.update()
    WIN.blit(ship, ship_center)
    WIN.blit(planet, planet_center)
    pygame.display.update()

def main():

    clock = pygame.time.Clock()

    run = True

    ship = Ship(SHIP, 2, 0.1, 300, 300, 0)
    p1 = Planet(400, PLANET, 0.5, HW, HH)
    ship.addPlanet(p1)

    bg_sprites = pygame.sprite.Group()

    for i in range(NUM_STARS):
        star = Star(r.randint(0, WIDTH),r.randint(0, HEIGHT), r.randint(15,50))
        bg_sprites.add(star)

    count = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        inputs = pygame.key.get_pressed()

        if inputs[pygame.K_LEFT]:
            ship.rotateImg(5)
        
        if inputs[pygame.K_RIGHT]:
            ship.rotateImg(-5)

        if inputs[pygame.K_SPACE]:
            ship.isAccelerating(True)
            ship.accelerate()
        else:
            ship.isAccelerating(False)

        ship.passiveMove()
        
        drawWindow(ship.getShip(), ship.getCoords(), p1.getImg(), p1.getRect(), bg_sprites, count)            

        count = (count % SPRITE_DELAY) + 1


    pygame.quit()

if __name__ == "__main__":
    main()