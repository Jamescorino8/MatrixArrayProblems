# Matrix Array Questions by James Corino
# Version 4/24/24

import random

array = []
n = random.randint(1, 9)

for x in range(n):
  r = []
  for y in range(n):
    r.append(random.randint(1, 9))
  array.append(r)

for x in range(n):
  print(array[x])

def colRtoL(array):
  for col in range(n - 1, -1, -1):
    for row in range(n):
      print(array[row][col])

def rowsAlt(array):
  for row in range(n):
    if (row % 2 == 0):
      for col in range(n):
        print(array[row][col])
    if (row % 2 != 0):
      for col in range(n - 1, -1, -1):
        print(array[row][col])

def spiral(array):
  col = 0
  row = 0
  colUpdate = 0
  rowUpdate = 0

  k = 0
  c = 0
  print(array[row][col])
  array[row][col] = -1
  col +=1
  while k != (n * n)-1:
    if c == 0:  #Right
      colUpdate = 1
      rowUpdate = 0
    elif c == 1:  #Down
      colUpdate = 0
      rowUpdate = 1
    elif c == 2:  #Left
      colUpdate = -1
      rowUpdate = 0
    elif c == 3:  #Up
      colUpdate = 0
      rowUpdate = -1
    while ((row < n) and (col < n) and (col >= 0) and (row >= 0) and (array[row][col] != -1)):
      print(array[row][col])
      array[row][col] = -1
      k += 1
      col += colUpdate
      row += rowUpdate
      
    if c == 0:  #Right
      col -= 1
      row += 1
    elif c == 1:  #Down
      row -= 1
      col -= 1
    elif c == 2:  #Left
      col += 1
      row -= 1
    elif c == 3:  #Up
      row += 1
      col += 1
      
    c += 1
    if c > 3:
      c = 0
    
#colRtoL(array)
#rowsAlt(array)
#spiral(array)