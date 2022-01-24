import sys

N = int(sys.stdin.readline())
graph = [int(sys.stdin.readline())for _ in range(N)]
mem = [0]*10001
counter = 0
mem[0] = graph[0]

if N>1:
    mem[1] = graph[0] + graph[1]

    for idx in range(2, N):
        if idx == 2:
            a, b, c = mem[0]+ graph[idx-1],mem[0]+graph[idx] ,graph[idx-1]+graph[idx]
            temp = max(a, b, c)
            if temp == a:
                counter = 0
            elif temp == b:
                counter = 1
            else:
                counter = 2
            mem[idx] = temp
            continue
        if counter <= 1:
            mem[idx] = mem[idx-1]+graph[idx]
            counter +=1
        else:
            a, b, c = mem[idx-1], graph[idx] + mem[idx-2], graph[idx] + mem[idx-3]
            temp_2 = max(mem[idx-1], graph[idx] + mem[idx-2], graph[idx] + mem[idx-3])
            mem[idx] = temp_2
            if temp_2 == a:
                counter = 0
            elif temp_2 == c:
                counter = -1
            else:
                counter = 1
    print(mem[:N])
    print(max(mem[:N]))
else:
    print(mem[0])