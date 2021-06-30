import pygame,math,os
from math import atan2, pi
from img import scaleImg

G = 8 # Gravitational constant

class Ship():

    def __init__(self, img, scale, accel, x, y, angle):
        self.img = scaleImg(img, scale)
        self.default = self.img
        self.accel = accel
        self.angle = angle
        self.rect = self.img.get_rect(center = (x,y))
        self.rotated = self.img
        self.mask = pygame.mask.from_surface(self.img)

        self.x_vel = 0
        self.y_vel = 0

        self.bodies = []

        self.frames = []
        self.frames.append(scaleImg(pygame.image.load(os.path.join('img', 'activeship1.png')), scale))
        self.frames.append(scaleImg(pygame.image.load(os.path.join('img', 'activeship2.png')), scale))
        self.frames.append(scaleImg(pygame.image.load(os.path.join('img', 'activeship3.png')), scale))
        self.frames.append(scaleImg(pygame.image.load(os.path.join('img', 'activeship4.png')), scale))

        self.current = 0
        self.image = self.frames[self.current]

    def isAccelerating(self, isAcc):
        if not isAcc:
            self.reset()

    def getRect(self):
        return self.rect

    def rotateImg(self, angle):
        self.angle += angle
        self.rotated = pygame.transform.rotozoom(self.img, self.angle, 1)
        self.rect = self.rotated.get_rect(center = self.rect.center)

    def accelerate(self):

        angle_rad = self.angle * math.pi / 180
        self.y_vel += self.accel * math.cos(angle_rad)
        self.x_vel += self.accel * math.sin(angle_rad)

        self.current += 1

        if self.current >= len(self.frames):
            self.current = 0

        self.rotated = pygame.transform.rotozoom(self.frames[self.current], self.angle, 1)

    def reset(self):
        self.rotated = pygame.transform.rotozoom(self.img, self.angle, 1)

    def passiveMove(self):
        # get forces from planets here
        for planet in self.bodies:
            center = planet.getCenter()
            pRect = planet.getRect()
            vec = self.vectorComp(center[0], center[1])
            offset = (pRect.topleft[0] - self.rect.topleft[0], pRect.topleft[1] - self.rect.topleft[1])

            if self.mask.overlap(planet.getMask(), offset):
                self.x_vel, self.y_vel = 0, 0
            else:
                theta = atan2(vec[1],vec[0])
                theta %= 2*pi

                m = planet.getMass()

                self.x_vel -= G * m * math.cos(theta) / (vec[0]**2 + vec[1]**2)
                self.y_vel -= G * m * math.sin(theta) / (vec[0]**2 + vec[1]**2)




            

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


    
    