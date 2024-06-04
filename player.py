import pygame
import math


class Player:
    def __init__(self, sprite, scale, position, original_image):
        self.sprite = pygame.transform.scale(sprite, scale)
        self.scale = scale
        self.position = position
        self.rect = sprite.get_rect(center=position, size=scale)
        self.x = self.position[0]
        self.y = self.position[1]
        self.original_image = original_image

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.sprite = pygame.transform.rotate(self.original_image, int(angle - 90))
        self.rect = self.sprite.get_rect(center=self.rect.center)

