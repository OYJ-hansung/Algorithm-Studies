import sys

dot, line, start = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(line)]
graph2 = [[]for _ in range(dot+1)]
for dot1, dot2 in graph:
    if dot1 not in graph2[dot2]:
        graph2[dot2].append(dot1)
    if dot2 not in graph2[dot1]:
        graph2[dot1].append(dot2)

for idx in graph2:
    idx.sort()


visited = [False]*(dot+1)

def DFS(graph, visited, dot):
    visited[dot] = True
    print(dot, end=' ')

    for idx in graph[dot]:
        if not visited[idx]:
            DFS(graph, visited, idx)

DFS(graph2, visited, start)