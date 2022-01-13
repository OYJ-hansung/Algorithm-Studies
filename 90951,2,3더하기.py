import sys

N = int(sys.stdin.readline())
graph = [int(sys.stdin.readline()) for _ in range(N)]
mem = [1, 2, 4]

def dynamic_programming(num):
    if num >= len(mem):
        for idx in range(len(mem), num):
            mem.append(mem[idx-1]+mem[idx-2]+mem[idx-3])
    print(mem[num-1])

for idx in graph:
    dynamic_programming(idx)

