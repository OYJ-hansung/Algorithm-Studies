import sys

N = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
mem = [0]*1001
mem[0] = [1, graph[0]]
for idx in range(1, N):
    target = graph[idx]
    try:
        temp = list(filter(lambda x: x[1] < target, mem[:idx]))
        mem[idx] = [max(temp)[0]+1, target]
    except:
        mem[idx] = [1, target]
print(mem[:N])
print(max(mem[:N])[0])


