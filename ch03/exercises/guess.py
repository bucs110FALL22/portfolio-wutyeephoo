import random

list = (range(1, 11))
secretnumber = int(random.choice(list))

number = int(input("Enter the guessing number: "))

if number == secretnumber:
    print("You guessed it")
else:
    if number != secretnumber:
        for i in range(1, 3):
            number = int(input("Enter the guessing number: "))
            if number < secretnumber:
                print("Too low")
            else:
                if number > secretnumber:
                    print("Too high")

#  FROM PROF: Your works, except if they don't get it on the first try,
#  they won't get a success message
#  This should always give a success message
                 # I see, thank you I will try this code instead
#     import random
#     list = (range(1, 11))
#     secretnumber = int(random.choice(list))
#     for i in range(1, 3):
#       number = int(input("Enter the guessing number: "))
#       if number < secretnumber:
#           print("Too low")
#       elif number > secretnumber:
#           print("Too high")
#       elif number == secretnumber:
#           print("You guessed it")
#           break
