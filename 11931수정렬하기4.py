import sys
import heapq

N = int(sys.stdin.readline())
graph = [int(sys.stdin.readline())for _ in range(N)]
heapq.heapify(graph)
graph = heapq.nlargest(N,graph)
print()
for idx in graph:
    print(idx)