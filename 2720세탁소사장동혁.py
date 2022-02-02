#  25, 10, 5, 1
import sys

test_case = int(sys.stdin.readline())
change = [int(sys.stdin.readline().strip())for _ in range(test_case)]
quarter = 25
dime = 10
nikel = 5
penny = 1


for num in change:
    left_change = num
    if int(left_change//quarter) !=0:
        print(int(left_change//quarter), end=' ')
        left_change -= quarter*int(left_change//quarter)
    else:
        print(0, end = ' ')
    if int(left_change//dime) !=0:
        print(int(left_change//dime), end=' ')
        left_change -= dime*int(left_change//dime)
    else:
        print(0, end = ' ')
    if int(left_change//nikel) !=0:
        print(int(left_change//nikel), end=' ')
        left_change -= nikel*int(left_change//nikel)
    else:
        print(0, end = ' ')
    if int(left_change//penny) !=0:
        print(int(left_change//penny))
        left_change -= penny*int(left_change//penny)
    else:
        print(0)
    
    
