import sys

N = int(sys.stdin.readline())
graph = [int(sys.stdin.readline())for _ in range(N)]
mem = [0]*301
mem[0] = graph[0]

if N > 1:
    mem[1] = max(mem[0]+graph[1], graph[1])
    if N > 2:
        mem[2] = max(mem[0] + graph[2], graph[2]+graph[1])
        for idx in range(3, N):
            mem[idx] = max(graph[idx] + graph[idx-1] + mem[idx-3], graph[idx] + mem[idx-2])

print(mem[N-1])