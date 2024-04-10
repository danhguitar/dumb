import pygame
from engine import Engine


ENGINE = Engine()
SCREEN = ENGINE.Window()
CLOCK = pygame.time.Clock()

PLAYER_IMAGE = pygame.image.load("assets/block.png").convert()

class player(ENGINE.Object):
  def __init__(self, x=10, y=10):
    ENGINE.Object.__init__(self, image=PLAYER_IMAGE, coordinates=(x, y))
    self.movespeed = 5

  def move(self, direction):
    if direction == "right":
      self.rect.x += self.movespeed
    if direction == "left":
      self.rect.x -= self.movespeed
    if direction == "down":
      self.rect.y += self.movespeed
    if direction == "up":
      self.rect.y -= self.movespeed

PLAYER = player(x=100, y=100)

while(True):
  for ev in pygame.event.get():
    if ev.type == pygame.QUIT:
      pygame.quit()
      quit()

  keys = pygame.key.get_pressed()

  if keys[pygame.K_a]: PLAYER.move("left")
  if keys[pygame.K_d]: PLAYER.move("right")
  if keys[pygame.K_s]: PLAYER.move("down")
  if keys[pygame.K_w]: PLAYER.move("up")

  if keys[pygame.K_ESCAPE]: ENGINE.raiseErr("you pressed esc, bro")


  SCREEN.fill()
  ENGINE.drawText(int(CLOCK.get_fps()), window=SCREEN)
  SCREEN.blit(PLAYER.image, PLAYER.get_coordinates())
  ENGINE.updateScreen()
  CLOCK.tick()