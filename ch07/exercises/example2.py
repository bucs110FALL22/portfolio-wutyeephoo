import pygame

class Player(pygame.sprite.Sprite):
  def__init__(self):
    super().__init__(self)
    self.health = 3
    self.direction = 3
    self.image = pygame.image.load("assets/hero.png")
    self.rect = self.image.get_rect()
    self.speed = 1

  def move_up(self):
    self.rect.y -= self.speed
    
  def.move_down(self):
    self.rect.y += self.speed
    
  def.move_right(self):
    self.rect.x += self.speed
    
  def.move_left(self):
    self.rect.x -= self.speed

  def fight(self, opponent):
    return random.randrange(3)
