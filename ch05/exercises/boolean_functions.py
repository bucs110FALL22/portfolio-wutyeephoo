def percentage_to_letter(score=0, letter=None):
  if score<60:
    letter = "F"
  elif score>=60 and score<70:
    letter = "D"
  elif score>=70 and score<80:
    letter = "C"
  elif score>=80 and score<90:
    letter = "B"
  elif score>=90:
    letter = "A"
  return(letter)
  
def is_passing(letter=None):
  if letter<="C":
    b = True
  else:
    b = False
  return b


score = float(input("Please enter your exam score: "))

letter = percentage_to_letter(score)
print("your grade is:" + letter)
print(is_passing(letter))