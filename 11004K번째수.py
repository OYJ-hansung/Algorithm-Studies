import sys

N, target = map(int, sys.stdin.readline().split())
graph = list(map(int, sys.stdin.readline().split()))
graph.sort()
print(graph[target-1])