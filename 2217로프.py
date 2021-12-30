import sys
from bisect import bisect_left
N = int(sys.stdin.readline())   
graph = [int(sys.stdin.readline())for _ in range(N)]
graph.sort()
answer = max(map(lambda x: x*(N - bisect_left(graph, x)), graph))
print(answer)



