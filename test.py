import sys
from collections import deque
from pprint import pprint

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip()))for _ in range(N)]

def BFS(x, y):
    q = deque()
    q.append([x, y])
    count = 1

    while q:
        x, y = q.popleft()
        for dx, dy in [[0,1], [0, -1], [1, 0], [-1, 0]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] == 1:
                    print(nx, ny, count)
                    count +=1
                    graph[nx][ny] = 9
                    q.append([nx, ny])
    print(count,'<<')
    danji_count.append(count)
    print()

danji = 0
danji_count = []

for row in range(N):
    for col in range(N):
        if graph[row][col] ==1:
            danji +=1
            BFS(row, col)

danji_count.sort()

print(danji)
for count in danji_count:
    print(count)

pprint(graph, width = 50)