import sys

N = int(sys.stdin.readline())
graph = [list(map(str, sys.stdin.readline().split()))for _ in range(N)]
graph.sort(key = lambda x: x[0])
graph.sort(key = lambda x: int(x[3]), reverse=True)
graph.sort(key = lambda x: int(x[2]))
graph.sort(key = lambda x: int(x[1]), reverse=True)
for name in graph:
    print(name[0])