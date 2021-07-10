import pygame
from img import scaleImg

class Planet(pygame.sprite.Sprite):
    def __init__(self, mass, img, scale, x, y, is_end):
        super().__init__()

        self.is_end = is_end

        self.mass = mass
        self.image = scaleImg(img, scale)
        self.rect = self.image.get_rect(center = (x,y))

        self.radius = int(self.rect.width * 0.7 / 2)
        
    def getBorder(self):
        return self.border

    def getImg(self):
        return self.image

    def getRect(self):
        return self.rect

    def getCenter(self):
        return self.rect.center

    def getMass(self):
        return self.mass

    def isEnd(self):
        return self.is_end
