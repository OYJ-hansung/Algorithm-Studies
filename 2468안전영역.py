from pydoc import visiblename
import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[0 for _ in range(N)]for _ in range(N)]
max_number = 0
min_number = 101

for idx in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    max_number = max(max(row), max_number)
    min_number = min(min(row), min_number)
    graph[idx] = row


def BFS(x, y, level):
    visited[x][y] = True
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny] and graph[nx][ny]>level:
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return 1

max_answer = 1
for level in range(min_number, max_number):
    visited = [[False for _ in range(N)]for _ in range(N)]
    answer = 0
    for x in range(N):
        for y in range(N):
            if not visited[x][y] and graph[x][y]>level:
                answer +=BFS(x, y, level)
    max_answer = max(answer, max_answer)

print(max_answer)

