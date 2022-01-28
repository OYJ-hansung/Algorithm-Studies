import sys
import heapq

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
graph.sort()
heap = []
heapq.heappush(heap, graph[0][1])

for meeting in graph[1:]:
    if meeting[0] < heap[0]:
        heapq.heappush(heap, meeting[1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, meeting[1])
print(len(heap))