import sys

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
print(graph)
mem = [0]*501
mem[0] = graph[0][0]
if N>1:
    mem[1] = list(map(lambda x: mem[0]+x ,graph[1]))
    print(mem[:2])

    for idx in range(2, N):
        print('current', idx)
        for i in range(len(graph[idx])):
            if i == 0:
                mem[idx] = [mem[idx-1][0]+graph[idx][i]]
            elif i == len(graph[idx])-1:
                mem[idx].append(mem[idx-1][-1]+graph[idx][i])
            else:
                print(mem[idx])
                num = max(mem[idx-1][i]+graph[idx][i], mem[idx-1][i-1]+graph[idx][i])
                mem[idx].append(num)
    print(mem[:N])
    print(max(mem[N-1]))
else:
    print(mem[0])