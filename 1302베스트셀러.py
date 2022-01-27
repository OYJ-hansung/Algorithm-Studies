import sys
from bisect import bisect_left, bisect_right
N = int(sys.stdin.readline())
graph = [sys.stdin.readline().strip() for _ in range(N)]
answer = -1
graph.sort()

def bisection(title):
    a = bisect_right(graph, title)
    b = bisect_left(graph, title)
    return a-b

for idx in graph:
    if bisection(idx) > answer:
        answer = bisection(idx)
        real_answer = idx

print(real_answer)