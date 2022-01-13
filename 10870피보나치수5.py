import sys

N = int(sys.stdin.readline())
mem = [0]*21
mem[0], mem[1], mem[2] = 0, 1, 1

for idx in range(3, N+1):
    mem[idx] = mem[idx-1] + mem[idx-2]

print(mem[N])

