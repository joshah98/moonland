import pygame
from img import scaleImg

class Planet:
    def __init__(self, mass, img, scale, x, y):
        self.mass = mass
        self.img = scaleImg(img, scale)
        self.rect = self.img.get_rect(center = (x,y))
        
        self.mask = pygame.mask.from_surface(self.img)

    def getBorder(self):
        return self.border

    def getImg(self):
        return self.img

    def getRect(self):
        return self.rect

    def getCenter(self):
        return self.rect.center

    def getMass(self):
        return self.mass

    def getMask(self):
        return self.mask
