import pygame,math,os
from math import atan2, pi
from img import scaleImg
from pygame_functions import *

G = 8 # Gravitational constant

class Ship(pygame.sprite.Sprite):

    def __init__(self, img, scale, accel, x, y, angle):
        super().__init__()
        
        self.img = scaleImg(img, scale)
        self.default = self.img
        self.accel = accel
        self.angle = angle
        self.rect = self.img.get_rect(center = (x,y))
        self.rotated = self.img
        self.collided = False

        self.radius = int(self.rect.width * 0.75 / 2)

        self.x_vel = 0
        self.y_vel = 0

        self.bodies = []

        self.frames = []
        self.frames.append(scaleImg(pygame.image.load(os.path.join('img', 'activeship1.png')), scale))
        self.frames.append(scaleImg(pygame.image.load(os.path.join('img', 'activeship2.png')), scale))
        self.frames.append(scaleImg(pygame.image.load(os.path.join('img', 'activeship3.png')), scale))
        self.frames.append(scaleImg(pygame.image.load(os.path.join('img', 'activeship4.png')), scale))

        self.explosion = []
        self.explosion.append(scaleImg(pygame.image.load(os.path.join('img', 'explosion1.png')), scale))
        self.explosion.append(scaleImg(pygame.image.load(os.path.join('img', 'explosion2.png')), scale))
        self.explosion.append(scaleImg(pygame.image.load(os.path.join('img', 'explosion3.png')), scale))
        self.explosion.append(scaleImg(pygame.image.load(os.path.join('img', 'explosion4.png')), scale))
        self.explosion.append(scaleImg(pygame.image.load(os.path.join('img', 'explosion5.png')), scale))
        self.explosion.append(scaleImg(pygame.image.load(os.path.join('img', 'explosion6.png')), scale))
        self.explosion.append(scaleImg(pygame.image.load(os.path.join('img', 'explosion7.png')), scale))
        self.explosion.append(scaleImg(pygame.image.load(os.path.join('img', 'explosion8.png')), scale))
        self.explosion.append(scaleImg(pygame.image.load(os.path.join('img', 'explosion9.png')), scale))
        self.explosion.append(scaleImg(pygame.image.load(os.path.join('img', 'explosion10.png')), scale))
        self.explosion.append(scaleImg(pygame.image.load(os.path.join('img', 'explosion11.png')), scale))

        self.explosion_frame = 0

        self.rubble = scaleImg(pygame.image.load(os.path.join('img', 'rubble.png')), scale)

        self.current = 0
        self.image = self.frames[self.current]

    def isAccelerating(self, isAcc):
        if not isAcc:
            self.reset()

    def getRect(self):
        return self.rect

    def getRadius(self):
        return self.radius

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
            vec = self.vectorComp(center[0], center[1])

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

    def stop(self):
        self.x_vel, self.y_vel = 0, 0

    def explode(self):
        if self.explosion_frame < len(self.explosion):
            self.rotated = pygame.transform.rotozoom(self.explosion[self.explosion_frame], self.angle, 1)

            # Delay between each tick to make frames easier to see
            # This can be delayed because no other processes need to happen simultaneously during this animation,
            # as opposed to the acceleration animation
            pygame.time.wait(40)
            self.explosion_frame += 1
        else:
         self.rotated = pygame.transform.rotozoom(self.rubble, self.angle, 1)



    
    