print(10 * 5)
print(10 ** 2)
print(15 / 10)
print(15 // 10)
print(-15 // 10)
print(15 % 10)
print(10 % 15)
print(10 % 10)
print(0 % 10)
print(10 / 15)
# 10 is smaller than 15 so 0 is output

rate = input("Enter the current exchange rate for Euro to Dollar: ")
rate = float(rate)

amount = input("Enter the amount of currency you wish to exchange: ")
amount = float(amount)

total = rate * amount
result = total - 3
print(result)                    