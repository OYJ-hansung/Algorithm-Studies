import sys

N = int(sys.stdin.readline())
if N == 1:
    print(0)
else:
    mem = [0]* (N+1)
    mem[1], mem[2]= 0, 1

    if N >=3:
        for idx in range(3, N+1):
            if idx%2 == 0 and idx%3 ==0:
                mem[idx] = min(mem[int(idx/2)]+1, mem[int(idx/3)]+1)
            elif idx%3 == 0:
                mem[idx] = min(mem[int(idx/3)]+1, mem[idx-1]+1)   
            elif idx%2 == 0:
                mem[idx] = min(mem[int(idx/2)]+1, mem[idx-1]+1)
            else:
                mem[idx] = mem[idx-1]+1

    print(mem[N])

