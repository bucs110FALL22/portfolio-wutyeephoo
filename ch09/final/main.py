import random 
import NationalHolidayAPI #Proxy Class
str input
def main():
    #Proxy Class
    day = NationalHolidayAPI.NationalHolidayAPI()
    input = day.get()
    for holiday in input:
        
        if input = holiday['national_holiday']:
          print("This date is a national holiday")
          holiday_facts = input
      
          fact = random.shuffle(holiday['holiday_facts'])

          print(fact)
      
main()