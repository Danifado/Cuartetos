import pygame

class Menu(pygame.sprite.Sprite):

    def __init__(self):
        self.imgs = [pygame.image.load("Assets/background.jpg")]
        self.index = 0
        self.move = 2
        self.img = self.imgs[self.index]
    def update(self):
        if self.index > 0:
            self.index = 0
        self.img = self.imgs[self.index]
        self.index += 1

    def draw(self, surface):
        if self.move > 1:
            surface.blit(self.img,(-1,-1))
            self.update()
