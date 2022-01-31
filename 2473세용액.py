import sys

N = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
graph.sort()
print(graph)

fixed = 0
left = fixed +1
right = N-1

for idx in graph[:N-2]:
    fixed_num = graph[fixed]
    while left < right:
        
