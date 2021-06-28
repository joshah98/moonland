import pygame,math
from math import atan2, pi
from img import scaleImg

G = 8 # Gravitational constant

class Ship:

    def __init__(self, img, scale, accel, x, y, angle):
        self.img = scaleImg(img, scale)
        self.accel = accel
        self.angle = angle
        self.rect = self.img.get_rect()
        self.rect.center = (x,y)
        self.rotated = self.img

        self.x_vel = 0
        self.y_vel = 0

        self.bodies = []

    def rotateImg(self, angle):
        self.angle += angle
        self.rotated = pygame.transform.rotozoom(self.img, self.angle, 1)
        self.rect = self.rotated.get_rect(center = self.rect.center)

    def accelerate(self):
        angle_rad = self.angle * math.pi / 180
        self.y_vel += self.accel * math.cos(angle_rad)
        self.x_vel += self.accel * math.sin(angle_rad)

    def passiveMove(self):
        # get forces from planets here
        for planet in self.bodies:
            center = planet.getCenter()
            vec = self.vectorComp(center[0], center[1])

            theta = atan2(vec[1],vec[0])
            theta %= 2*pi

            self.x_vel -= G * planet.getMass() * math.cos(theta) / (vec[0]**2 + vec[1]**2)
            self.y_vel -= G * planet.getMass() * math.sin(theta) / (vec[0]**2 + vec[1]**2)

        self.rect.y -= self.y_vel
        self.rect.x -= self.x_vel

    def addPlanet(self, planet):
        self.bodies.append(planet)    

    def vectorComp(self, x, y):
        delta_x = x - self.rect.x
        delta_y = y - self.rect.y
        return (delta_x, delta_y)

    def getShip(self):
        return self.rotated

    def getCoords(self):
        return (self.rect.x,self.rect.y)

    
    