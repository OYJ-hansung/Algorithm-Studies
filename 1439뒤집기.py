import sys

graph = list(map(int, sys.stdin.readline().strip()))
current = 9
one = 0
zero = 0
flag = False

for idx in graph:
    if idx != current and idx == 0:
        zero +=1
        current = 0
    elif idx != current and idx == 1:
        one +=1
        current = 1
print(min(zero, one))



