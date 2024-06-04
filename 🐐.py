import pygame


class Lebron:
    def __init__(self, sprite, scale, position, original_image):
        self.sprite = pygame.transform.scale(sprite, scale)
        self.scale = scale
        self.position = position
        self.rect = sprite.get_rect(center=position, size=scale)
        self.x = self.position[0]
        self.y = self.position[1]
        self.original_image = original_image
        print(self.position)
