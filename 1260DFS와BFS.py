import sys
from collections import deque
dots, lines, start = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(dots+1)]

for idx in range(lines):
    dot1, dot2 = map(int, sys.stdin.readline().split())
    graph[dot1].append(dot2)
    graph[dot2].append(dot1)

for idx in graph:
    idx.sort()

def BFS(graph, start):
    visited = [False]*(dots+1)
    visited[start] = True
    q = deque()
    q.append(start)

    while q:
        dot = q.popleft()
        print(dot, end=' ')
        for idx in graph[dot]:
            if not visited[idx]:
                visited[idx] = True
                q.append(idx)



def DFS(graph, dot, visited):
    visited[dot] = True
    DFS_list.append(dot)

    for idx in graph[dot]:
        if not visited[idx]:
            DFS(graph, idx, visited)

DFS_list = []
visited = [False]*(dots+1)
DFS(graph, start, visited)
print(* DFS_list)
BFS(graph, start)