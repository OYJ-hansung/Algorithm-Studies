import sys
from collections import deque

col, row , height = map(int, sys.stdin.readline().split())

graph = [[]for _ in range(height)]

for idx in range(height):
    temp = [list(map(int, sys.stdin.readline().split()))for _ in range(row)]
    graph[idx] = temp

def BFS(z, x, y):
    
    visited[z][x][y] = True
    q= deque()
    q.append([z, x, y])
    while q:
        z, x, y = q.popleft()
        for dx, dy, dz in [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]:
            nx = x + dx
            ny = y + dy
            nz = z + dz
            if 0<=nx<row and 0<=ny<col and 0<=nz<height:
                if not visited[nz][nx][ny] and graph[nz][nx][ny] == 0:
                    visited[nz][nx][ny] = True
                    graph[nz][nx][ny] = graph[z][x][y] + 1
    return 1

def check_if():
    for floor in graph:
        for row in floor:
            if 0 in row:
                return False
    return True

day = 1
while True:
    if check_if():
        print(0)
        break

    visited = [[[False for _ in range(col)]for _ in range(row)]for _ in range(height)]
    count = 0
    for z in range(height):
        for x in range(row):
            for y in range(col):
                if not visited[z][x][y] and graph[z][x][y] == day:
                        count += BFS(z, x, y)

    day +=1
    if check_if():
        print(day-1)
        break
    elif count == 0:
        print(-1)
        break