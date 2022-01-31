import sys

N = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().split())for _ in range(N)]

graph.sort(key=lambda x: (int(x[3]),int(x[2]),int(x[1])))
print(graph[-1][0])
print(graph[0][0])
