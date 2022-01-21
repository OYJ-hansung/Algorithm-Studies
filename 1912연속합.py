import sys

N = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
mem = [0]*100001
mem[0] = graph[0]
sum = 0
flag = False

if N >1:
    for idx in range(1, N):
        if mem[0] <0 and graph[idx]<0 and flag == False:
            mem[idx] = graph[idx]
            continue
        elif mem[idx-1]<0 and graph[idx]>0:
            mem[idx] = graph[idx]
            flag = True
            continue
        
        sum = mem[idx-1] + graph[idx]
        if sum >= 0 or (sum<0 and graph[idx]<0):
            mem[idx] = mem[idx-1] + graph[idx]
        else:
            mem[idx] = graph[idx]
    print(mem[:N])
    print(max(mem[:N]))
else:
    print(mem[0])

    