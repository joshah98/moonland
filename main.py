from level_select import level_select
from img import scaleImg
import pygame
import os
from button import Button
from level import level

# Define window
WIDTH, HEIGHT = 1800, 1000
HW, HH = WIDTH/2, HEIGHT/2
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images
START = scaleImg(pygame.image.load(os.path.join('img', 'start.png')), 4)
START_RECT = START.get_rect()
START_HOVER = scaleImg(pygame.image.load(os.path.join('img', 'start_hover.png')), 4)
START_CLICK = scaleImg(pygame.image.load(os.path.join('img', 'start_clicked.png')), 4)

# Define colors
WHITE = (255,255,255)
BLUE = (0,0,20)

def main():

    run = True

    while run:
        ## Start screen
        WIN.fill(BLUE)
        start = Button(HW, HH, START, START_HOVER, START_CLICK)
        
        if start.handle_click(WIN):

            ## Level select screen
            level_select(WIN, HW, HH)
        
        for event in pygame.event.get():
            # Handle x-ing out of game
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()

    pygame.quit()

    


if __name__ == "__main__":
    main()