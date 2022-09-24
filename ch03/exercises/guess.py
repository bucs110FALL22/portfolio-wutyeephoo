import random
list = (range(1, 11))
secretnumber = int(random.choice(list))

for i in range(3):
  number = int(input("Enter the guessing number: "))

if number < secretnumber:
  print("Too low")
elif number > secretnumber:
  print("Too high")
elif number == secretnumber:
  print("You guessed it")
