import pygame
import os
from ship import Ship
from planet import Planet
import math


WIDTH, HEIGHT = 1800, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255,255,255)
BLUE = (0,0,100)
FPS = 60

SHIP = pygame.image.load(os.path.join('img', 'ship.png'))
PLANET = pygame.image.load(os.path.join('img', 'planet1.png'))


pygame.display.set_caption("moonland")


def drawWindow(ship, ship_center, planet, planet_center):
    WIN.fill(BLUE)
    WIN.blit(ship, ship_center)
    WIN.blit(planet, planet_center)
    pygame.display.update()

def main():

    clock = pygame.time.Clock()

    run = True

    ship = Ship(SHIP, 0.25, 0.1, 300, 300, 0)
    p1 = Planet(400, PLANET, 1, 500, 700)
    ship.addPlanet(p1)

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
            ship.accelerate()

        ship.passiveMove()
        
        drawWindow(ship.getShip(), ship.getCoords(), p1.getImg(), p1.getRect())


    pygame.quit()

if __name__ == "__main__":
    main()