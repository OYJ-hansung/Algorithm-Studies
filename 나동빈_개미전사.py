import sys

N = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
dynamic_graph = [0]*N

dynamic_graph[0] = graph[1]
dynamic_graph[1] = max(dynamic_graph[0], graph[1])
for idx in range(3, N):
    dynamic_graph[idx] = max(dynamic_graph[idx-1], dynamic_graph[idx-2]+graph[idx])

print(dynamic_graph[N-1])