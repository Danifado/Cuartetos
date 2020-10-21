import pygame, os

class Card(pygame.sprite.Sprite):

    def __init__(self, value):
        self.valor = value
        self.imgs = [pygame.image.load("Carta_{0}.png".format(str(self.valor)))]
        self.index = 0
        self.move = 2
        self.img = self.imgs[self.index]

    def update(self):
        if self.index > 0:
            self.index = 0
        self.img = self.imgs[self.index]
        self.index += 1

    def draw(self, surface, pos):
        if self.move > 1:
            surface.blit(self.img,pos)
            self.update()
