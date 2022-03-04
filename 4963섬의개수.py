import sys
from collections import deque

def BFS(x, y):
    visited[x][y] = True
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, -1], [-1, 1]]:
            nx = x +dx
            ny = y +dy
            if 0<=nx<row and 0<=ny<col:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return 1

answer_list = []
while True:
    col, row = map(int, sys.stdin.readline().split())
    if col == 0 and row == 0:
        break

    graph = [list(map(int, sys.stdin.readline().split()))for _ in range(row)]
    visited = [[False for _ in range(col)]for _ in range(row)]

    answer = 0
    for x in range(row):
        for y in range(col):
            if not visited[x][y] and graph[x][y] == 1:
                answer += BFS(x, y)
    print(answer)

