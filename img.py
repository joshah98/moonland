import pygame

def scaleImg(img, factor):
    rect = img.get_rect()
    img = pygame.transform.scale(img, (int(rect[2]*factor), int(rect[3]*factor)))
    return img