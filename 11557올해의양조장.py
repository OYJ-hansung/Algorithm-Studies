import sys

N = int(sys.stdin.readline())
for _ in range(N):
    K = int(sys.stdin.readline())
    graph = [list(sys.stdin.readline().split()) for _ in range(K)]
    graph.sort(key=lambda x: int(x[1]))
    print(graph)
    print('answer', graph[-1][0])

