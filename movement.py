import pygame

def rotateImg(surface, angle):
    rotated = pygame.transform.rotozoom(surface, angle, 1)
    new_rect = rotated.get_rect(center = (300,300))
    return rotated, new_rect