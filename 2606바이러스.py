from collections import deque
import sys

N = int(sys.stdin.readline())
line = int(sys.stdin.readline())
graph = [[]for _ in range(N+1)]

for idx in range(line):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def BFS(graph, start):
    answer = 0
    visited = [False]* (N+1)
    visited[start] = True
    q = deque()
    q.append(start)

    while q:
        dot = q.popleft()
        for idx in graph[dot]:
            if not visited[idx]:
                visited[idx] = True
                q.append(idx)
                answer +=1

    return answer

print(BFS(graph, 1))