import pygame

from enginefiles.obj import Obj
from enginefiles.error import ERROR
from enginefiles.window import Display

pygame.init()

class Engine():
  def __init__(self):
    self.font = pygame.font.Font("assets/font.ttf", 15)

  def drawText(self, text="filler text", location=(10, 10), window=pygame.display):
    text_display = self.font.render(str(text), True, "white")
    return window.blit(text_display, location)

  def nuObj(self, image, x=10, y=10):
    return Obj(image=image, x=x, y=y)

  def changeFont(self, font):
    self.font = font

  def raiseErr(self, message):
    ERROR(message)

  class Object(Obj):
    def __init__(self, image, coordinates=(10, 10)):
      Obj.__init__(self, image=image, x=coordinates[0], y=coordinates[1])
  
  class Window(Display):
    def __init__(self, size=(800, 600)):
      Display.__init__(self, size)