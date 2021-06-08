import pygame
import os

WIDTH, HEIGHT = 1800, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255,255,255)
BLUE = (0,0,100)
FPS = 60

def scaleImg(img, factor):
    rect = img.get_rect()
    img = pygame.transform.scale(img, (int(rect[2]*factor), int(rect[3]*factor)))
    return img


ACTIVE_SHIP = pygame.image.load(os.path.join('img', 'activeship.png'))
ACTIVE_SHIP = scaleImg(ACTIVE_SHIP, 0.25)
SHIP = pygame.image.load(os.path.join('img', 'ship.png'))
SHIP = scaleImg(SHIP, 0.25)

pygame.display.set_caption("moonland")


def drawWindow():
    WIN.fill(BLUE)
    WIN.blit(SHIP, (450,250))
    pygame.display.update()

def main():

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        drawWindow()


    pygame.quit()

if __name__ == "__main__":
    main()