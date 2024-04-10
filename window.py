import pygame


class Display():  
  def __init__(self, size=(800, 600)):
    self = pygame.display.set_mode(size=size)
  
  def updateScreen(self):
    pygame.display.flip()

  def fill(self, color=(0,0,0)):
    self.fill(color)