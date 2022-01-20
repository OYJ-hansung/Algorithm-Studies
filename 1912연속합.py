import sys

N = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
mem = [0]*100001
mem[0] = graph[0]
sum = 0
k = 1
if N >1:
    for idx in range(k, N):
        if mem[0] <0 and graph[idx]<0:
            continue
        if mem[0] <0 and graph[1]>0:
            mem[1] = graph[1]
            continue
        sum = mem[idx-1] + graph[idx]
        if sum >= 0:
            mem[idx] = mem[idx-1] + graph[idx]
        else:
            mem[idx] = graph[idx]
    print(max(mem[:N]))
else:
    print(mem[0])