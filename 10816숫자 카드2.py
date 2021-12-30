import sys
from bisect import bisect_left, bisect_right

def count(graph, value):
    right_index = bisect_right(graph, value)
    left_index = bisect_left(graph, value)
    return right_index - left_index

N = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
graph.sort()
I = int(sys.stdin.readline())
answer = list(map(lambda x: count(graph, int(x)), sys.stdin.readline().split()))

for i in answer:
    print(i, end=' ')





