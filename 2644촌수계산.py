import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
person1, person2 = map(int, sys.stdin.readline().split())
line = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for idx in range(line):
    A, B = map(int, sys.stdin.readline().split())
    if A not in graph[B]:
        graph[B].append(A)
    if B not in graph[A]:
        graph[A].append(B)

visited = [False]*(N+1)
depth = [0]*(N+1)
depth[0] = -1

def DFS(graph, visited, start, before):
    visited[start] = True
    depth[start] = depth[before] +1

    for idx in graph[start]:
        if not visited[idx]:
            DFS(graph, visited, idx, start)

DFS(graph, visited, person1, 0)
if depth[person2] == 0:
    print(-1)
else:
    print(depth[person2])