import sys

col, row = map(int, sys.stdin.readline().split())
answer = 1

if col >=3 and row >=7:
    answer = row-2
elif col>=3 and row <7:
    if row<5:
        answer = row
    else:
        answer = 4
elif col==2 and row>=2:
    answer = int(row//2)
    if (row%2)!=0:
        answer +=1
    if answer >4:
        answer = 4
else:
    answer = 1

print(answer)

