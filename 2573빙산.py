from collections import deque
import sys
from pprint import pprint

row, col = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(row)]


def DFS(graph, visited, melt, x, y):
    visited[x][y] = True

    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nx = x + dx
        ny = y + dy
        if 0<=nx<row and 0<=ny<col:
            if graph[nx][ny] !=0:
                if visited[nx][ny] == False:
                    DFS(graph, visited, melt, nx, ny)
            else:
                melt[x][y] +=1
    return True

def BFS(graph, visited, melt, a,b):
    visited[a][b] = True
    q = deque()
    q.append([a, b])

    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<row and 0<=ny<col:
                if graph[nx][ny] !=0:
                    if visited[nx][ny] == False:
                        visited[nx][ny] = True
                        q.append([nx, ny])
                else:
                    melt[x][y] +=1
    return True

year = 0
while True:
    melt = [[0 for _ in range(col)]for _ in range(row)]
    visited = [[False for _ in range(col)]for _ in range(row)]
    glacier = 0
    for x in range(row):
        for y in range(col):
            if not visited[x][y] and graph[x][y] != 0:
                if BFS(graph, visited, melt, x, y):
                    glacier +=1

    if glacier == 0:
        print(0)
        break
    elif glacier >1:
        print(year)
        break
    
    for x in range(row):
        for y in range(col):
            if graph[x][y] > melt[x][y]:
                graph[x][y] -= melt[x][y]
            else:
                graph[x][y] = 0
    year +=1
    