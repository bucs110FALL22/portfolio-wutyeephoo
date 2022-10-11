def star_pyramid():
  rows = int(input("Enter the number of rows: "))
  count = 0
  while count <= rows:
    print('*'*count)
    count += 1
star_pyramid()

def rstar_pyramid():
  rows = int(input("Enter the number of rows: "))
  count = rows
  while count >= 0:
    print('*'*count)
    count -= 1
rstar_pyramid()