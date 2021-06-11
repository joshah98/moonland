import pygame
from img import scaleImg

class Planet:
    def __init__(self, mass, img, scale, x, y):
        self.mass = mass
        self.img = scaleImg(img, scale)
        self.center = (x,y)


    def getImg(self):
        return self.img

    def getCenter(self):
        return self.center

    def getMass(self):
        return self.mass