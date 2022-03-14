import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip()))for _ in range(row)]

def BFS(x, y):
    visited = [[[0]*2 for _ in range(col)]for _ in range(row)]
    visited[x][y][0] = 1
    q = deque()
    q.append([x, y, 0])

    while q:
        x, y, depth = q.popleft()
        if x == row-1 and y == col-1:
            return visited[x][y][depth]
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<row and 0<=ny<col:
                if visited[nx][ny][depth]==0 and graph[nx][ny] == 0:
                    visited[nx][ny][depth] = visited[x][y][depth] +1
                    q.append([nx, ny, depth])
                elif graph[nx][ny] ==1 and depth==0:
                    visited[nx][ny][depth+1] = visited[x][y][depth] +1
                    q.append([nx, ny, depth+1])
    return -1

answer_list = []
print(BFS(0, 0))
