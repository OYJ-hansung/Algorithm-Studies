from collections import deque
import sys

dots, lines = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(dots+1)]

for idx in range(lines):
    dot1, dot2 = map(int,sys.stdin.readline().split())
    graph[dot1].append(dot2)
    graph[dot2].append(dot1)

def BFS(dot):
    visited[dot] = True
    q = deque()
    q.append(dot)

    while q:
        dot = q.popleft()
        for idx in graph[dot]:
            if not visited[idx]:
                visited[idx] = True
                q.append(idx)
    return 1

answer = 0
visited = [False]*(dots+1)
for x in range(1,dots):
    if not visited[x]:
        answer += BFS(x)

print(answer)
