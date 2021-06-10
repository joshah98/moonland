import pygame, math

def scaleImg(img, factor):
    rect = img.get_rect()
    img = pygame.transform.scale(img, (int(rect[2]*factor), int(rect[3]*factor)))
    return img

class Ship:
    def __init__(self, img, scale, velocity, x, y, angle):
        self.img = scaleImg(img, scale)
        self.velocity = velocity
        self.angle = angle
        self.rect = self.img.get_rect()
        self.rect.center = (x,y)
        self.rotated = self.img

    def rotateImg(self, angle):
        self.angle += angle
        self.rotated = pygame.transform.rotozoom(self.img, self.angle, 1)
        self.rect = self.rotated.get_rect(center = self.rect.center)

    def forward(self):
        angle_rad = self.angle * math.pi / 180
        self.rect.y -= self.velocity * math.cos(angle_rad)
        self.rect.x -= self.velocity * math.sin(angle_rad)
      

    def getShip(self):
        return self.rotated

    def getCoords(self):
        return (self.rect.x,self.rect.y)

    
    