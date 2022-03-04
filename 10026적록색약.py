from collections import deque
import sys
from pprint import pprint

N = int(sys.stdin.readline())
graph_RGB = [[0 for _ in range(N)]for _ in range(N)]
graph_RG = [[]for _ in range(N)]

for idx in range(N):
    row = list(sys.stdin.readline().strip())
    graph_RGB[idx] = row

    for i in range(N):
        if row[i] == 'B':
            graph_RG[idx].append('B')
        else:
            graph_RG[idx].append('R')



def BFS(x, y, color, graph):
    visited[x][y] = True
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N  and 0<=ny<N:
                if graph[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return 1
    
answer_RGB = 0
visited = [[False for _ in range(N)]for _ in range(N)]
for color in ['R', 'B', 'G']:
    for x in range(N):
        for y in range(N):          
            if not visited[x][y] and graph_RGB[x][y]==color:
                answer_RGB += BFS(x, y, color, graph_RGB)
print(answer_RGB, end=' ')

answer_RG = 0
visited = [[False for _ in range(N)]for _ in range(N)]
for color in ['R', 'B']:
    for x in range(N):
        for y in range(N):          
            if not visited[x][y] and graph_RG[x][y]==color:
                answer_RG += BFS(x, y, color, graph_RG)

print(answer_RG)
