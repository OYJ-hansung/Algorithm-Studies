import sys

N = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
graph_set = sorted(set(graph))

for idx in graph_set:
    print(idx, end=' ')
