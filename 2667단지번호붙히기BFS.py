import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip()))for _ in range(N)]

def BFS(graph, x, y):
    global count
    q = deque()
    q.append([x, y])
    graph[x][y] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx = x +dx
            ny = y +dy
            if 0<=nx<N and 0<=ny<N and graph[nx][ny] ==1:
                graph[nx][ny] = 0
                count +=1
                q.append([nx, ny])


danji = 0
count_list = []
for x in range(N):
    for y in range(N):
        if graph[x][y] !=0:
            count = 1
            BFS(graph, x,y)
            danji +=1
            count_list.append(count)

count_list.sort()

print(danji)
for idx in count_list:
    print(idx)