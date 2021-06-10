import pygame
import os
from movement import rotateImg


def scaleImg(img, factor):
    rect = img.get_rect()
    img = pygame.transform.scale(img, (int(rect[2]*factor), int(rect[3]*factor)))
    return img

WIDTH, HEIGHT = 1800, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255,255,255)
BLUE = (0,0,100)
FPS = 60

ACTIVE_SHIP = pygame.image.load(os.path.join('img', 'activeship.png'))
ACTIVE_SHIP = scaleImg(ACTIVE_SHIP, 0.25)
SHIP = pygame.image.load(os.path.join('img', 'ship.png'))
SHIP = scaleImg(SHIP, 0.25)

# dimensions of ship
rect = SHIP.get_rect()
SHIP_X = rect[2]
SHIP_Y = rect[3]

pygame.display.set_caption("moonland")


def drawWindow(ship, ship_rect):
    WIN.fill(BLUE)
    WIN.blit(ship, (ship_rect.x, ship_rect.y))
    pygame.display.update()

def main():

    angle = 0
    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        inputs = pygame.key.get_pressed()

        rotated_ship, rotated_rect = rotateImg(SHIP, angle)

        if inputs[pygame.K_LEFT]:
            angle += 5
        elif inputs[pygame.K_RIGHT]:
            angle -= 5


        drawWindow(rotated_ship, rotated_rect)


    pygame.quit()

if __name__ == "__main__":
    main()