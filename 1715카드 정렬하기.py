import sys
import heapq


N = int(sys.stdin.readline())
graph = [int(sys.stdin.readline())for _ in range(N)] 
answer = 0 
result = 0

while len(graph) != 1:
    a = heapq.heappop(graph)
    b = heapq.heappop(graph)
    result += a+b
    heapq.heappush(graph, a+b)
print(result)

