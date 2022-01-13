import sys

N = int(sys.stdin.readline())
mem = [0]*1001
mem[0], mem[1], mem[2] = 1, 2, 3

for idx in range(3, N+1):
    mem[idx] = mem[idx-1] + mem[idx-2]

answer = mem[N-1]%10007
print(answer)

