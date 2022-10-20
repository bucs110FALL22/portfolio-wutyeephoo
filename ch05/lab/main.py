import pygame
iters = {}
upper_limit = 20

#n = int(input("Input a number: "))
#print(n)

for i in range (2, upper_limit+1):
  n = i
  count = 0
  
while(n != 1):
  if(n % 2) == 0:
    n = n//2
  else:
    n = 3*n + 1
  count += 1
  iters[i] = (count)
  #iters.update({couny: count})

print(iters)

#int max_so_far;