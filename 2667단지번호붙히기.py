import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip()))for _ in range(N)]
visited = [[False for _ in range(N)]for _ in range(N)]

def BFS(x,y):
    answer = 1
    visited[x][y] = True
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny]=True
                    q.append([nx, ny])
                    answer +=1
    return answer

danji = 0
cnt_list = []
for x in range(N):
    for y in range(N):
        if not visited[x][y] and graph[x][y] == 1:
            cnt = BFS(x, y)
            cnt_list.append(cnt)
            danji+=1

print(danji)
cnt_list.sort()
for idx in cnt_list:
    print(idx)

