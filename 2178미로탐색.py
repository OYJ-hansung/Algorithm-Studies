import sys
from collections import deque
row, col = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip()))for _ in range(row)]
visited = [[False for _ in range(col)]for _ in range(row)]

def BFS(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [0, -1], [1,0],[-1,0]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<row and 0<=ny<col:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])

BFS(0,0)
print(graph[row-1][col-1])