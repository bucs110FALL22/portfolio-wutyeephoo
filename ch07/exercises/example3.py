import pygame
import random

class Player(pygame.sprite.Sprite):
  def__init__(self):
    super().__init__(self)
    self.health = 3
    self.direction = 3
    self.image = pygame.image.load("assets/hero.png")
    self.rect = self.image.get_rect()
    self.speed = 1