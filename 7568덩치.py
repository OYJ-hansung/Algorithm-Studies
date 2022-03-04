import sys

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
answer = []

for a, b in graph:
    temp = 1
    for x, y in graph:
        if a<x and b<y:
            temp +=1
    answer.append(temp)

print(*answer)