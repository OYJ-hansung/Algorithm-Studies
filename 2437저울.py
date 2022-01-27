import sys
N = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
graph.sort()

if graph[0] != 1 or N == 1:
    print(1)
else:
    for idx in range(N):
        summation = sum(graph[:idx+1])
        if idx == N-1:
            print(summation+1)
            break
        if summation < graph[idx+1] and (summation*2) != graph[idx+1] and (summation+1) !=graph[idx+1]:
            print(summation+1)
            break