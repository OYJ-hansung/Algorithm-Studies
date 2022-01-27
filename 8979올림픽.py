import sys

N, K = map(int,sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
graph.sort(key=lambda x: x[3], reverse=True)
graph.sort(key=lambda x: x[2], reverse=True)
graph.sort(key=lambda x: x[1], reverse=True)
print(graph)
for idx in range(N):
    if graph[idx][0] == K:
        if graph[idx][1:] == graph[idx-1][1:]:
            print(idx)
            print('YES!')
        else:
            print(idx+1)
        break
