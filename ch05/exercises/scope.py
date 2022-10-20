def multiplier(number1, number2):
  result = 0 #accumulator - starting value is zero
  for i in range(number2):
      result += number1
  return result

def exponential(number, exponent):
  result = 1 #accumulator - starting value is zero
  for i in range(exponent):
      result *= number
  return result

def square(number):
  return(multiplier(number, number))

def main():
  print(multiplier(5, 7))
  print(exponential(3, 2))
  print(square(4))
main()