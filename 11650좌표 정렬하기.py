import sys

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

graph.sort(key = lambda x:x[1])
graph.sort()

for idx in graph:
    print(idx[0], idx[1])

