import sys
from collections import deque

T = int(sys.stdin.readline())
print()

def BFS(x, y):
    graph[x][y] = 0
    q = deque()
    q.append([x,y])

    while q:
        x, y = q.popleft()
        for dx, dy in[[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<row and 0<=ny<col:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append([nx, ny])
    return 1


for _ in range(T):
    col, row, num = map(int,sys.stdin.readline().split())
    graph = [[0 for _ in range(col)]for _ in range(row)]
    answer = 0

    for _ in range(num):
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
    
    for x in range(row):
        for y in range(col):
            if graph[x][y] == 1:
                answer += BFS(x, y)
                
    print(answer)


