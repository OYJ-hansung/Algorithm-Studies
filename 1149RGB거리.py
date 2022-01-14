import sys

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]

for idx in range(1, len(graph)):
    graph[idx][0] = min(graph[idx-1][1], graph[idx-1][2]) + graph[idx][0]
    graph[idx][1] = min(graph[idx-1][0], graph[idx-1][2]) + graph[idx][1]
    graph[idx][2] = min(graph[idx-1][1], graph[idx-1][0]) + graph[idx][2]

print(min(graph[N-1]))

