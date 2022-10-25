numbers = [[10, 11, 12, 13, 14],
          [20, 21, 22, 23, 24],
          [30, 31, 32, 33, 34]]

rnum = len(numbers)
cnum  = len(numbers[0])

for i in range (rnum):
  rsum = 0
  for j in range (cnum):
    rsum += numbers[i][j]
  print("The summation of each row {0}: {1}".format(i, rsum))


