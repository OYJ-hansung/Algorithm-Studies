import sys
from copy import deepcopy
from itertools import combinations
from collections import deque

row, col = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(row)]

#BFS 바이러스 수 탐색
def BFS(x, y):
    global virus
    visited[x][y] = True
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<row and 0<=ny<col and copy_graph[nx][ny] == 0:
                copy_graph[nx][ny] = 2
                virus +=1
                visited[nx][ny] = True
                q.append([nx, ny])

# 그래프 그리기 / 0개수 세기
zero_list = []
first_virus = 0
for i in range(row):
    new_row = list(map(int, sys.stdin.readline().split()))
    for idx in range(col):
        if new_row[idx] == 0:
            zero_list.append([i, idx])
        if new_row[idx] == 2:
            first_virus +=1
    graph[i] = new_row

#완전탐색 - 벽 세우기 / 딥카피
zero = len(zero_list) -3
combination_list = list(combinations(zero_list, 3))
safety_zone = -1

for [x1, y1], [x2, y2], [x3, y3] in combination_list:
    copy_graph = deepcopy(graph)
    copy_graph[x1][y1], copy_graph[x2][y2], copy_graph[x3][y3] = 1, 1, 1
    visited = [[False for _ in range(col)]for _ in range(row)]

    virus = -first_virus
    for x in range(row):
        for y in range(col):
            if copy_graph[x][y] == 2 and not visited[x][y]:
                virus +=1
                BFS(x, y)
    safety_zone = max((zero - virus), safety_zone)

print(safety_zone)