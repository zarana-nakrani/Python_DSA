"""
*****
****
***
**
*
"""
def pattern_printing():
    for row in range(0,5):
        for col in range(5, row, -1):
            print("*", end=" ")
        print("\n")
# pattern_printing()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

def pattern2():
    for row in range(0, 6):
        for col in range(1, row+1):
            print(col, end=" ")
        print("\n")
# pattern2()

"""
n = 5
*
**
***
****
*****
****
***
**
*
"""

def pattern3(n):
    for row in range(1, 2*n):
        col = 0
        # if row > n:
        #     col = 2*n - row
        # else:
        #     col = row
        col = 2*n - row if row > n else row
        for c in range(1, col+1):
            print("* ", end=" ")
        print("\n")
# pattern3(5)

"""
n = 5
    1  
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1  
"""
def pattern4(n):
    for row in range(2 * n):
        col = (2*n - row) - 1 if row >= n else row + 1
        spaces = (row - n) + 1 if row >= n else (n - row) - 1
        for i in range(spaces):
            print(" ", end="")
        for c in range(1, col+1):
            print(c, end=" ")
        print("\n")
# pattern4(5)

"""
n = 5
rows = 9
        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
  4 3 2 1 2 3 4
    3 2 1 2 3
      2 1 2
        1
"""

def pattern5(n):
    for row in range(1, 2*n):
        for spaces in range((2*n - row)+1):
            print(" ", end="")
        for col in range(n-, , -1):
            print(col, end=" ")
        for col in range(2, row+1):
            print(col, end=" ")
        print("\n")

pattern5(5)