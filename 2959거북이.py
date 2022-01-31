import sys

graph = list(map(int, sys.stdin.readline().split()))
graph.sort()
print(graph[0] *graph[2])
