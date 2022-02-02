import sys
from pprint import pprint

def flip(x,y,array):
    for i in range(3):
        for d in range(3):
            array[x+i][y+d] = 1-array[x+i][y+d]


row, col = map(int, sys.stdin.readline().split())
matrix_given = [list(map(int, sys.stdin.readline().strip()))for _ in range(row)]
matrix_target = [list(map(int, sys.stdin.readline().strip()))for _ in range(row)]
answer = 0

for starting_row in range(row-2): #3
    for starting_col in range(col-2): #4
        if matrix_given[starting_row][starting_col] != matrix_target[starting_row][starting_col]:
            answer +=1
            flip(starting_row, starting_col, matrix_given)

if matrix_given == matrix_target:
    print(answer)
else:
    print(-1)