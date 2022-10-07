import random
import pygame
import math

pygame.init()
window = pygame.display.set_mode()
windowsize = pygame.display.get_window_size()

window.fill('lightblue')
centerx = windowsize[0]/2
centery = windowsize[1]/2
radius = centery
pygame.draw.circle(window, 'red', (centerx,centery), radius)
pygame.draw.line(window, 'black', [0, centery], [windowsize[0], centery])
pygame.draw.line(window, 'black', [centerx, 0], [centerx, windowsize[1]])
print(windowsize[0])
print(windowsize[1])

x = random.randrange(0, windowsize[0])
y = random.randrange(0, windowsize[1])

#pygame.draw.circle(window, 'black', (x,y), 2)

distance_from_center = math.hypot(windowsize[0]/2-x, windowsize[1]/2-y)
print(distance_from_center)

player1 = 0
player2 = 0
player1color = 'green'
player2color = 'purple'
outsidecolor = 'pink'

bet = int(input("Select  player 1 or 2: "))

is_in_circle = distance_from_center <= radius
print(is_in_circle)
for i in range(10):
  
  #player 1
  x = random.randrange(0, windowsize[0])
  y = random.randrange(0, windowsize[1])
  distance_from_center = math.hypot(windowsize[0]/2-x, windowsize[1]/2-y)
  if distance_from_center < radius:
    pygame.draw.circle(window, player1color, (x,y), 2)
    player1 += 1
  else:
    pygame.draw.circle(window, outsidecolor, (x,y), 2)
  
  # player 2
  x = random.randrange(0, windowsize[0])
  y = random.randrange(0, windowsize[1])
  pygame.draw.circle(window, 'black', (x,y), 2)
  distance_from_center = math.hypot(windowsize[0]/2-x, windowsize[1]/2-y)
  if distance_from_center < radius:
    pygame.draw.circle(window, player2color, (x,y), 2)
    player2 += 1
  else:
    pygame.draw.circle(window, outsidecolor, (x,y), 2)
  pygame.display.flip()
if player1 > player2:
  print("Player 1 is the winner")
  print("you won the bet") if bet == 1 else print("you bet badly")
elif player1 < player2:
  print("Player 2 is the winner")
  print("you won the bet") if bet == 2 else print("you bet badly")
elif player1 == player2:
  print("It's a tie")

pygame.time.wait(10000)