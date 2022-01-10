import sys

N = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
d = [0]*N

d[0] = graph[0]
d[1] = max(graph[0], graph[1])

for idx in range(3, N):
    d[idx] = max(d[idx-1], d[idx-2] + graph[idx])

print(d[N-1])

