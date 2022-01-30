import sys
import heapq

N = int(sys.stdin.readline())
graph = list(map(lambda x: int(x),sys.stdin.readline().split()))
for idx in range(1,N):
    graph.extend(list(map(int,sys.stdin.readline().split())))
    graph = heapq.nlargest(N, graph)

print(graph[-1])