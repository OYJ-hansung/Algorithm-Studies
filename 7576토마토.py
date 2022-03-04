from pprint import pprint
import sys
from collections import deque

col, row = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(row)]

q = deque()
for x in range(row):
    for y in range(col):
        if graph[x][y] == 1:
            q.append([x,y])

def DFS():
    while q:
        x, y = q.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<row and 0<=ny<col:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])


year = 1     
flag = True
DFS()
for row in graph:
    year = max(max(row), year)
    if 0 in row:
        print(-1)
        flag = False
        break
if flag:
    print(year-1)