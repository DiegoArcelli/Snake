import pygame


class Piece(pygame.sprite.Sprite):

    def __init__(self, pos, cycles):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.cycle = cycles

    def decreaseCycle(self):
        self.cycle -= 1
        return self.cycle

    def getPosition(self):
        return self.rect.center
