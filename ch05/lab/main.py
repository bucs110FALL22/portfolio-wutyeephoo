import pygame
iters = {}
n = int(input("Input a number: "))
print(n)
upper_limit = 20
couny = 1

for i in range (2, upper_limit+1):
  count = 0
  couny += 1
  
while(n != 1):
  if(n % 2) == 0:
    n = n//2
    print(n)
  else:
    n = 3*n + 1
    print(n)
  count += 1
  iters[n] = (count)
  #iters.update({couny: count})

print(iters)

#int max_so_far;